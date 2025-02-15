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
import screen
import utils
import app
import ads_screens
import settings


class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.add_widget(self.layout)

        self.add_widget(MDLabel(text="Inscription", halign="center", pos_hint={"center_x": 0.5, "top": 0.9}))

        self.name_field = MDTextField(hint_text="Nom", size_hint=(None, None), size=("280dp", "48dp"), pos_hint={"center_x": 0.5, "top": 0.75})
        self.layout.add_widget(self.name_field)

        self.email_field = MDTextField(hint_text="Email", size_hint=(None, None), size=("280dp", "48dp"), pos_hint={"center_x": 0.5, "top": 0.65})
        self.layout.add_widget(self.email_field)

        self.password_field = MDTextField(hint_text="Mot de passe", size_hint=(None, None), size=("280dp", "48dp"), pos_hint={"center_x": 0.5, "top": 0.55}, password=True)
        self.layout.add_widget(self.password_field)

        self.signup_button = MDRaisedButton(text="S'inscrire", size_hint=(None, None), size=("280dp", "48dp"), pos_hint={"center_x": 0.5, "top": 0.4}, on_release=self.register_user)
        self.layout.add_widget(self.signup_button)

        self.back_button = MDRaisedButton(text="Retour", size_hint=(None, None), size=("100dp", "48dp"), pos_hint={"x": 0, "top": 1}, on_release=self.go_back)
        self.layout.add_widget(self.back_button)


    def register_user(self, instance):
        name = self.name_field.text
        email = self.email_field.text
        password = self.password_field.text

        if name and email and password:
            user_data = {"name": name, "email": email, "password": password}
            utils.save_user_to_json(user_data)
            print(f"Utilisateur inscrit : {name}, {email}")
            self.manager.current = "main"
        else:
            print("Veuillez remplir tous les champs")

    def go_back(self, instance):
        # Retourner à l'écran principal
        self.manager.current = "main"