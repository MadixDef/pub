import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate('firebase_credentials.son')
firebase_admin.initialize_app(cred)


def send_push_notification(title, body, token):
    message = messaging.Message(
        notification=messaging.Notification(title=title, body=body),
        token=token,
    )
    response = messaging.send(message)
    return response
