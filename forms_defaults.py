import json
import os
from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/forms.body',
    'https://www.googleapis.com/auth/drive',
]

DRIVE_FOLDER_NAME = 'Formulários de Atividades Sonho Meu'
TEMPLATE_FORM_ID = '1397ryjvN6OJBraxPXrjhdbz88ejgIQeMAFAGxSruSpg'

QUIZ_SETTINGS = {
    'isQuiz': True,
}

EMAIL_COLLECTION_TYPE = 'VERIFIED'


def get_credentials():
    creds = None
    token_path = 'token.json'

    if os.path.exists(token_path):
        with open(token_path, encoding='utf-8') as token_file:
            stored_scopes = json.load(token_file).get('scopes', [])
        if not set(SCOPES).issubset(set(stored_scopes)):
            os.remove(token_path)
        else:
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError:
                if os.path.exists(token_path):
                    os.remove(token_path)
                creds = None

        if not creds:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return creds


def get_drive_folder_id(drive_service, folder_name):
    escaped_name = folder_name.replace("'", "\\'")
    query = (
        f"name='{escaped_name}' "
        "and mimeType='application/vnd.google-apps.folder' "
        "and trashed=false"
    )
    results = drive_service.files().list(
        q=query,
        spaces='drive',
        fields='files(id, name)',
        pageSize=10,
        includeItemsFromAllDrives=True,
        supportsAllDrives=True,
    ).execute()
    folders = results.get('files', [])
    if folders:
        return folders[0]['id']

    folder = drive_service.files().create(
        body={
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
        },
        fields='id',
        supportsAllDrives=True,
    ).execute()
    return folder['id']


def move_file_to_folder(drive_service, file_id, folder_id):
    file = drive_service.files().get(
        fileId=file_id,
        fields='parents',
        supportsAllDrives=True,
    ).execute()
    previous_parents = ','.join(file.get('parents', []))
    drive_service.files().update(
        fileId=file_id,
        addParents=folder_id,
        removeParents=previous_parents,
        fields='id, parents',
        supportsAllDrives=True,
    ).execute()


def build_choice_question(question):
    return {
        "createItem": {
            "item": {
                "title": question["title"],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [{"value": opt} for opt in question["options"]],
                        },
                        "grading": {
                            "pointValue": question["points"],
                            "correctAnswers": {
                                "answers": [{"value": question["correct"]}]
                            },
                            "whenWrong": {"text": question["when_wrong"]},
                        },
                    }
                },
            },
            "location": {"index": question["index"]},
        }
    }


def create_quiz_form(title, document_title):
    creds = get_credentials()
    form_service = build('forms', 'v1', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)

    copied = drive_service.files().copy(
        fileId=TEMPLATE_FORM_ID,
        body={'name': document_title},
        fields='id',
        supportsAllDrives=True,
    ).execute()
    form_id = copied['id']

    form_service.forms().batchUpdate(
        formId=form_id,
        body={
            "requests": [
                {
                    "updateFormInfo": {
                        "info": {"title": title},
                        "updateMask": "title",
                    }
                },
                {
                    "updateSettings": {
                        "settings": {
                            "quizSettings": QUIZ_SETTINGS,
                            "emailCollectionType": EMAIL_COLLECTION_TYPE,
                        },
                        "updateMask": "quizSettings.isQuiz,emailCollectionType",
                    }
                },
            ]
        },
    ).execute()

    folder_id = get_drive_folder_id(drive_service, DRIVE_FOLDER_NAME)
    move_file_to_folder(drive_service, form_id, folder_id)

    form = form_service.forms().get(formId=form_id).execute()
    return form_service, form
