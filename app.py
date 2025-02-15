import json
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
import login_screen
import signup_screen
import utils
import screen
import ads_screens
import settings
import screen


# Écran principal avec menu latéral
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_email = None
        self.user_name = None
        self.is_user_logged_in = None

        # Layout principal
        self.layout = FloatLayout()
        self.add_widget(self.layout)

        # Barre d'outils en haut avec bouton de menu
        self.toolbar = MDTopAppBar(
            title="Accueil",
            pos_hint={"top": 1},
            elevation=10,
            left_action_items=[["menu", lambda x: self.toggle_nav_drawer()]]  # Bouton de menu (☰)
        )
        self.layout.add_widget(self.toolbar)

        # Texte de bienvenue au centre
        self.welcome_label = MDLabel(
            text="Bienvenue!",
            halign="center",
            size_hint=(None, None),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.layout.add_widget(self.welcome_label)

    def toggle_nav_drawer(self):
        """Ouvre ou ferme la barre latérale."""
        if self.manager and hasattr(self.manager, "nav_drawer"):
            self.manager.nav_drawer.set_state("toggle")

    def update_ui(self):
        """Met à jour l'interface en fonction de l'état de connexion."""
        if self.is_user_logged_in:
            # Mettre à jour le texte de bienvenue avec le nom de l'utilisateur
            self.welcome_label.text = f"Bienvenue, {self.user_name}!"
        else:
            # Réinitialiser le texte de bienvenue
            self.welcome_label.text = "Bienvenue!"

    def logout_user(self, instance):
        """Déconnecte l'utilisateur et met à jour l'interface."""
        if self.is_user_logged_in:
            # Enregistrer l'action de déconnexion
            utils.log_user_action(self.user_email, "logout", {"status": "success"})

        self.is_user_logged_in = False
        self.user_name = ""
        self.user_email = ""  # Réinitialiser l'email
        self.update_ui()

# Application principale
if __name__ == "__main__":
    screen.MainApp().run()