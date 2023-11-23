import requests
import zipfile
import io
import xml.etree.ElementTree as ET
from Classe.Coordonnees import Coordonnees
from helper import trier, selectionner_n_premiers
import json
from geopy.geocoders import Nominatim
from InquirerPy import inquirer
from API.importation_toutes_donnees import trouver_stations_par_filtres
from API.convertion import adresse_en_coordonnees


class RechercheView:
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "adresse",
                "message": "Entrez votre adresse :",
            },
            {
                "type": "checkbox",
                "name": "services",
                "message": "Sélectionnez les services recherchés :",
                "choices": [
                    {"name": "Station de gonflage"},
                    {"name": "Station de lavage"},
                    {"name": "Piste poids lourds"},
                    {"name": "Vente de gaz domestique (Butane, Propane)"},
                    {"name": "DAB (Distributeur automatique de billets)"},
                    {"name": "Boutique alimentaire"},
                    {"name": "Restauration à emporter"},
                    {"name": "Bornes électriques"},
                    {"name": "Automate CB 24/24"},
                    {"name": "Vente d'additifs carburants"},
                    {"name": "Relais colis"},
                    {"name": "Services réparation / entretien"},
                    {"name": "Location de véhicule"},
                    {"name": "Wifi"},
                    {"name": "Toilettes publiques"},
                    {"name": "Boutique non alimentaire"},
                    {"name": "Aire de camping-cars"},
                    {"name": "Espace bébé"},
                    {"name": "Douches"},
                    {"name": "Restauration sur place"},
                ],
            },
        ]

    def display_info(self):
        print("Bienvenue dans la recherche de stations !")

    def make_choice(self):
        answers = inquirer.prompt(self.__questions)
        adresse = answers["adresse"]
        services_recherches = answers.get("services", [])
        coor_utilisateur = adresse_en_coordonnees(adresse)

        if coor_utilisateur:
            trouver_stations_par_filtres(5, services_recherches, coor_utilisateur)
        else:
            print("Adresse non trouvée. Veuillez réessayer.")
