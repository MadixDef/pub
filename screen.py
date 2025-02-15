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
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.textfield import MDTextField
import login_screen
import signup_screen
import utils
import app
import ads_screens
import settings
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager
import login_screen
import signup_screen
import utils
import screen
import ads_screens
import settings


# Écran des catégories
class CategoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()  # Utilisation de FloatLayout ici
        self.add_widget(self.layout)

        # Titre de l'écran
        self.add_widget(MDLabel(text="Choisissez une catégorie", halign="center", size_hint=(None, None),
                                pos_hint={"center_x": 0.5, "top": 0.9}))
        # Boutons de catégories dans le corps de l'écran
        self.create_category_buttons()

        # Bouton retour en haut à gauche
        self.back_button = MDRaisedButton(
            text="Retour",
            size_hint=(None, None),
            size=("100dp", "48dp"),
            pos_hint={"x": 0, "top": 1},
            on_release=self.go_back
        )
        self.layout.add_widget(self.back_button)

    def create_category_buttons(self):
        # Liste des catégories à afficher sur le corps de l'écran
        categories = ["Communication", "Restauration", "Voiture", "Smartphone"]
        scroll = ScrollView()
        container = MDBoxLayout(orientation='vertical', size_hint_y=None)
        container.bind(minimum_height=container.setter('height'))

        for category in categories:
            button = MDRaisedButton(
                text=category,
                size_hint=(None, None),
                size=("280dp", "48dp"),
                on_release=lambda x, category=category: self.on_category_select(category)
            )
            container.add_widget(button)

        scroll.add_widget(container)
        self.layout.add_widget(scroll)

    def on_category_select(self, category):
        # Enregistrement de l'action, s'il y a un utilisateur connecté
        main_screen = self.manager.get_screen("main")
        if main_screen.is_user_logged_in:
            email = main_screen.user_email
            utils.log_user_action(email, "select_category", {"category": category})
        else:
            print("Aucun utilisateur connecté.")

        # Changement d'écran vers la publicité de la catégorie choisie
        print(f"Catégorie sélectionnée: {category}")
        self.manager.current = f"{category.lower()}_ads"

    def go_back(self, instance):
        # Retour à l'écran principal
        self.manager.current = "main"


# Application principale avec mise à jour dynamique du menu latéral
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"

        # Création du ScreenManager
        self.screen_manager = ScreenManager()

        # Création du MDNavigationLayout
        self.nav_layout = MDNavigationLayout()

        # Création du MDNavigationDrawer (menu latéral)
        self.nav_drawer = MDNavigationDrawer()

        # Création des contenus pour le menu latéral
        # Contenu par défaut du menu latéral : options globales
        self.nav_drawer_box = MDBoxLayout(orientation='vertical')
        self.default_nav_list = MDList()
        self.default_nav_list.add_widget(
            OneLineListItem(text="Catégories", on_release=lambda x: self.navigate_to("categories"))
        )
        self.default_nav_list.add_widget(
            OneLineListItem(text="Connexion", on_release=lambda x: self.navigate_to("login"))
        )
        self.default_nav_list.add_widget(
            OneLineListItem(text="Inscription", on_release=lambda x: self.navigate_to("signup"))
        )
        self.nav_drawer_box.add_widget(self.default_nav_list)

        # Contenu spécifique lorsque l'utilisateur est sur l'écran "Catégories"
        self.categories_nav_list = MDList()
        self.categories_nav_list.add_widget(
            OneLineListItem(text="Communication", on_release=lambda x: self.navigate_to("communication_ads"))
        )
        self.categories_nav_list.add_widget(
            OneLineListItem(text="Restauration", on_release=lambda x: self.navigate_to("restauration_ads"))
        )
        self.categories_nav_list.add_widget(
            OneLineListItem(text="Voiture", on_release=lambda x: self.navigate_to("voiture_ads"))
        )
        self.categories_nav_list.add_widget(
            OneLineListItem(text="Smartphone", on_release=lambda x: self.navigate_to("smartphone_ads"))
        )

        # Initialement, le menu latéral affiche le contenu par défaut
        self.nav_drawer_box_initial = self.default_nav_list
        self.nav_drawer.add_widget(self.nav_drawer_box)

        # Ajout du ScreenManager et du NavigationDrawer dans le NavigationLayout
        self.nav_layout.add_widget(self.screen_manager)
        self.nav_layout.add_widget(self.nav_drawer)

        # Ajout des différents écrans
        self.screen_manager.add_widget(app.MainScreen(name="main"))
        self.screen_manager.add_widget(CategoryScreen(name="categories"))
        self.screen_manager.add_widget(login_screen.LoginScreen(name="login"))
        self.screen_manager.add_widget(signup_screen.SignupScreen(name="signup"))
        # Ajout des écrans pour chaque catégorie de promotion
        for cat in ["communication", "restauration", "voiture", "smartphone"]:
            self.screen_manager.add_widget(ads_screens.AdsScreen(category=cat, name=f"{cat}_ads"))

        # Rendre le nav_drawer accessible via le screen_manager
        self.screen_manager.nav_drawer = self.nav_drawer

        return self.nav_layout

    def navigate_to(self, screen_name):
        """Navigue vers l'écran spécifié et met à jour le menu latéral en conséquence."""
        self.screen_manager.current = screen_name

        # Mise à jour du contenu du menu latéral en fonction de l'écran sélectionné
        # Si on navigue vers l'écran "catégories", afficher les catégories dans le menu latéral
        if screen_name == "categories":
            # Effacer le contenu et ajouter les catégories
            self.nav_drawer_box.clear_widgets()
            self.nav_drawer_box.add_widget(self.categories_nav_list)
        else:
            # Pour les autres écrans, afficher le contenu par défaut
            self.nav_drawer_box.clear_widgets()
            self.nav_drawer_box.add_widget(self.default_nav_list)

        self.nav_drawer.set_state("close")  # Ferme le menu latéral

