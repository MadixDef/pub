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
import utils
import screen
import ads_screens



# Fonction pour récupérer les publicités spécifiques à la catégorie
def get_promotions_by_category(category):
    # Exemple : Filtrer les promotions en fonction de la catégorie
    return [("1", "Publicité exemple 1", "Offre spéciale 20% de réduction")]  # Pour l'exemple

