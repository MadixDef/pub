import json
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import MDList
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import MDTextField
import login_screen
import signup_screen
import screen
import app
import ads_screens
import settings
from datetime import datetime

# Chemin du fichier de logs
LOGS_FILE = "user_actions.json"


def log_user_action(email, action, details=None):
    log_entry = {
        "email": email,
        "action": action,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "details": details
    }

    try:
        with open(LOGS_FILE, "r") as file:
            logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(log_entry)

    with open(LOGS_FILE, "w") as file:
        json.dump(logs, file, indent=4)

    print(f"Action enregistrée : {log_entry}")  # Debug


def read_users_from_json():
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    return users


# Fonction pour enregistrer un nouvel utilisateur
def save_user_to_json(user_data):
    users = read_users_from_json()
    users.append(user_data)
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)





