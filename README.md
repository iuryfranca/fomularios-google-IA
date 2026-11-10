# fomularios-google-IA

## Google credentials

The credential files stay only on your machine. They are listed in `.gitignore` and must never be committed.

| File | What it is | Used by |
| --- | --- | --- |
| `client_secrets.json` | OAuth client (Desktop app) | `forms_defaults.py`, to open the Google login |
| `token.json` | Access and refresh token of the logged-in account | `forms_defaults.py`, created automatically |
| `credentials.json` | Service account key | Not used by the scripts |

### How to get them again

All of them come from the [Google Cloud Console](https://console.cloud.google.com/), in the project used for these quizzes. The Google Forms API and the Google Drive API must be enabled in that project under [APIs & Services > Library](https://console.cloud.google.com/apis/library).

**`client_secrets.json`**

1. Open [APIs & Services > Credentials](https://console.cloud.google.com/apis/credentials).
2. Under "OAuth 2.0 Client IDs", open the Desktop app client and download the JSON.
3. If the download is not available, add a new client secret or create a new OAuth client ID of type "Desktop app", then download its JSON.
4. Save the file as `client_secrets.json` in the project root.

**`token.json`**

1. Make sure `client_secrets.json` is in the project root.
2. Run any quiz script, for example `python criar_quiz_html.py`.
3. A browser opens for the Google login. After you approve, `token.json` is created in the project root.

To log in with another account or renew the access, delete `token.json` and run a script again.

**`credentials.json`**

1. Open [IAM & Admin > Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts).
2. Open the service account, go to "Keys", then "Add key" > "Create new key" > "JSON".
3. Save the downloaded file as `credentials.json` in the project root.

An existing service account key cannot be downloaded a second time, so this always creates a new key. Delete the old key on the same screen.
