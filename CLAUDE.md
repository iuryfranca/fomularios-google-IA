# Google Forms quizzes — Fundação Sonho Meu

This repo creates graded Google Forms quizzes for Sonho Meu activities. The user sends lesson material (screenshots, slide text, notes, or a topic name). Turn that material into one Python script that creates the quiz. Do not invent a new architecture.

## How the user asks

Requests are usually informal and incomplete. Treat screenshots and pasted content as the source of truth.

- Screenshots of slides, handouts, or code examples are the lesson. Read every image. Extract definitions, tags, attributes, analogies, examples, and contrasts that a student should remember.
- Pasted text is the same material in writing. Merge it with the screenshots. If they disagree, prefer the screenshot of the slide the class actually saw.
- A short message such as "faz o quiz disso" means: build the full quiz from everything attached in that message.
- The user writes in Brazilian Portuguese. Questions, options, and feedback must be in Brazilian Portuguese. Code, file names, and commit messages stay in English.
- Do not ask the user to reformat the material. Ask only when a fact needed for a correct answer is missing or two sources contradict each other.

## What to turn into questions

Cover the whole lesson, not only the first slides. One question per important idea.

- Use the wording of the lesson so students recognize the concept. Do not add facts that are not in the material.
- Prefer concrete checks: what a tag does, which attribute holds a value, what an analogy maps to, which option matches a definition from the slide.
- Each question has exactly one correct answer and three plausible wrong answers. Wrong answers must be clearly false from the lesson, not trick wording.
- The correct value must match one option character for character.
- `when_wrong` is one short sentence that states the right idea, in the same language as the slides. It is shown when the student misses the question.
- Default to 5 points per question. Keep every question required.
- Aim for a full activity quiz, on the order of the existing scripts (about 15–25 questions), scaled to how much material was sent. Do not pad with repeated questions.

## How to build the form

Reuse `forms_defaults.py`. Do not copy auth, folder, or template logic into the quiz script.

- `create_quiz_form(title, document_title)` copies the template, turns the copy into a quiz, collects a verified email, and moves the file into the Drive folder `Formulários de Atividades Sonho Meu`.
- `build_choice_question` creates one required single-choice (`RADIO`) item with grading and `when_wrong`.
- `title` is what respondents see: `Quiz: Topic — Short subtitle`.
- `document_title` is the Drive file name: `Quiz_Topic_Slug` with underscores, no spaces.
- Add questions with one `batchUpdate`. Index them in list order starting at 0.

Create one new file per quiz: `criar_quiz_<topic>.py`. Follow `criar_quiz_html.py`. No comments in the code. Do not edit `forms_defaults.py` unless the shared helper cannot express the request. Do not create extra docs, helpers, or sample files.

Question object:

```python
{
    "title": "Question text?",
    "options": ["Correct option", "Wrong", "Wrong", "Wrong"],
    "correct": "Correct option",
    "points": 5,
    "when_wrong": "Short explanation of the correct idea.",
}
```

Script shape:

```python
from forms_defaults import DRIVE_FOLDER_NAME, build_choice_question, create_quiz_form

QUIZ_QUESTIONS = [
    # question dicts
]

def main():
    print("Criando o formulário...")
    form_service, form = create_quiz_form(
        "Quiz: Topic — Subtitle",
        "Quiz_Topic_Slug",
    )
    form_id = form["formId"]
    print(f"\nFormulário criado com sucesso!")
    print(f"Link para responder: {form['responderUri']}")
    print(f"Link para editar: https://docs.google.com/forms/d/{form_id}/edit")
    print(f'Formulário salvo na pasta "{DRIVE_FOLDER_NAME}".\n')

    requests = []
    for index, question in enumerate(QUIZ_QUESTIONS):
        requests.append(build_choice_question({**question, "index": index}))

    print("Adicionando perguntas...")
    form_service.forms().batchUpdate(formId=form_id, body={"requests": requests}).execute()
    print(f"Quiz criado com {len(QUIZ_QUESTIONS)} perguntas ({len(QUIZ_QUESTIONS) * 5} pontos no total).")

if __name__ == "__main__":
    main()
```

After writing the script, run it with `python criar_quiz_<topic>.py` and return the responder link and the edit link. The first run may open a browser for Google login; that is expected. Never print, commit, or rewrite `token.json`, `credentials.json`, or `client_secrets.json`.

## Scope

Change only the new quiz script unless the user asks for something else. Do not commit unless asked. Reply to the user in Brazilian Portuguese.
