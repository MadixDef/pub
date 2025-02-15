from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
import settings

class AdsScreen(Screen):
    def __init__(self, category, **kwargs):
        super().__init__(**kwargs)
        self.category = category
        self.layout = FloatLayout()  # Utilisation de FloatLayout ici aussi
        self.add_widget(self.layout)

        # Titre de la catégorie
        self.add_widget(
            MDLabel(text=f"Publicités pour {self.category.capitalize()}", halign="center", size_hint=(None, None),
                    pos_hint={"center_x": 0.5, "top": 0.9}))

        # Ajouter le bouton retour en haut à gauche
        self.back_button = MDRaisedButton(
            text="Retour",
            size_hint=(None, None),
            size=("100dp", "48dp"),
            pos_hint={"x": 0, "top": 1},  # Positionné en haut à gauche
            on_release=self.go_back,
            md_bg_color=(0.2, 0.6, 1, 1),  # Couleur de fond bleue
            theme_text_color="Custom",  # Permet de personnaliser la couleur du texte
            text_color=(1, 1, 1, 1)  # Texte blanc
        )
        self.layout.add_widget(self.back_button)



    def display_ads(self):
        # Affichage des publicités spécifiques à la catégorie
        ads = settings.get_promotions_by_category(self.category)
        scroll = ScrollView()
        container = MDBoxLayout(orientation='vertical', size_hint_y=None)
        container.bind(minimum_height=container.setter('height'))

        for ad in ads:
            container.add_widget(MDLabel(text=f"{ad[1]} - {ad[2]}", theme_text_color="Secondary"))

        scroll.add_widget(container)
        self.layout.add_widget(scroll)

    def go_back(self, instance):
        print("Tentative de retour vers les catégories...")  # Debug
        if self.manager:
            print(f"Écrans disponibles : {self.manager.screen_names}")  # Debug
            self.manager.current = "categories"
        else:
            print("Erreur : self.manager n'est pas défini.")  # Debug