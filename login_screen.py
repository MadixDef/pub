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
import screen
import signup_screen
import utils
import app
import ads_screens
import settings


def get_logged_in_user_email(self):
    main_screen = self.manager.get_screen("main")
    if main_screen.is_user_logged_in:
        return main_screen.user_email
    return None

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.add_widget(self.layout)

        self.add_widget(MDLabel(text="Connexion", halign="center", pos_hint={"center_x": 0.5, "top": 0.9}))

        self.email_field = MDTextField(hint_text="Email", size_hint=(None, None), size=("280dp", "48dp"),
                                       pos_hint={"center_x": 0.5, "top": 0.75})
        self.layout.add_widget(self.email_field)

        self.password_field = MDTextField(hint_text="Mot de passe", size_hint=(None, None), size=("280dp", "48dp"),
                                          pos_hint={"center_x": 0.5, "top": 0.65}, password=True)
        self.layout.add_widget(self.password_field)

        self.login_button = MDRaisedButton(text="Se connecter", size_hint=(None, None), size=("280dp", "48dp"),
                                           pos_hint={"center_x": 0.5, "top": 0.5}, on_release=self.login_user)
        self.layout.add_widget(self.login_button)

        self.back_button = MDRaisedButton(text="Retour", size_hint=(None, None), size=("100dp", "48dp"),
                                          pos_hint={"x": 0, "top": 1}, on_release=self.go_back)
        self.layout.add_widget(self.back_button)

    def login_user(self, instance):
        email = self.email_field.text
        password = self.password_field.text
        users = utils.read_users_from_json()

        for user in users:
            if user["email"] == email and user["password"] == password:
                print(f"Connexion réussie : {user['name']}")

                # Enregistrer l'action de connexion
                utils.log_user_action(email, "login", {"status": "success", "user_name": user["name"]})

                # Récupérer l'écran principal et mettre à jour l'état de connexion
                main_screen = self.manager.get_screen("main")
                main_screen.is_user_logged_in = True
                main_screen.user_email = email  # Définir l'email de l'utilisateur
                main_screen.user_name = user["name"]
                main_screen.update_ui()  # Mettre à jour l'interface
                self.manager.current = "main"
                return

        # Enregistrer une tentative de connexion échouée
        utils.log_user_action(email, "login", {"status": "failed"})
        print("Email ou mot de passe incorrect")

    def view_content(self, content_id):
        # Récupérer l'email de l'utilisateur connecté
        email = self.get_logged_in_user_email()  # Tu dois implémenter cette méthode
        if email:
            # Enregistrer l'action
            utils.log_user_action(email, "view_content", {"content_id": content_id})
        else:
            print("Aucun utilisateur connecté.")

    def view_category(self, category_name):
        # Récupérer l'email de l'utilisateur connecté
        email = self.get_logged_in_user_email()  # Tu dois implémenter cette méthode
        if email:
            # Enregistrer l'action
            utils.log_user_action(email, "view_category", {"category": category_name})
        else:
            print("Aucun utilisateur connecté.")

    def go_back(self, instance):
        self.manager.current = "main"
