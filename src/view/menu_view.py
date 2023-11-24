from InquirerPy import prompt
import requests

# import sys

# sys.path.insert(0, "\\filer-eleves2\id2315\projet_info\projet_info")
# from InquirerPy import prompt

# from InquirerPy import inquirer
from view.abstract_view import AbstractView
from view.session_view import Session
from DAO.inscriptionDAO import InscriptionDAO

# from DAO.MenuDAO import (
#     MenuDAO,
# )  # Créez votre propre DAO pour gérer les fonctionnalités du menu


class MenuView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choice",
                "message": "Que voulez-vous faire ?\n-----------------------------------",
                "choices": [
                    # "Effectuer une recherche",
                    # "Consulter mes stations favorites",
                    # "Modifier/Supprimer mes stations favorites",
                    # "Déconnexion",
                    {"name": "Effectuer une recherche", "value": "1"},
                    {"name": "Consulter mes stations favorites", "value": "2"},
                    {"name": "Modifier/Supprimer mes stations favorites", "value": "3"},
                    {"name": "Créer une liste de stations favorites", "value": "4"},
                    {"name": "Déconnexion", "value": "5"},
                ],
            },
        ]

    def display_info(self):
        print("Bienvenue dans le menu !")
        print("-----------------------------------")

    def make_choice(self):
        while True:
            answers = prompt(self.__questions)
            choice = answers["choice"]

            if choice == "1":
                # Appel à l'API pour obtenir toutes les listes favorites
                response = requests.get("http://127.0.0.1/listesFav/")
                if response.status_code == 200:
                    data = response.json()  # Récupérer les données JSON
                    print("Listes favorites disponibles:")
                    for key, value in data.items():
                        print(f"{key}: {value}")
                else:
                    print("Erreur lors de la récupération des listes favorites.")

            elif choice == "2":
                # Appel à l'API pour obtenir une liste spécifique
                numero = int(input("Entrez le numéro de la liste: "))
                response = requests.get(f"http://127.0.0.1/listesFav/{numero}")
                if response.status_code == 200:
                    data = response.json()  # Récupérer les données JSON
                    print(f"Liste favorite {numero}: {data}")
                else:
                    print(f"Erreur lors de la récupération de la liste {numero}.")

            elif choice == "3":
                # Ajoutez le code pour l'option "Modifier/Supprimer mes stations favorites"
                pass

            elif choice == "4":
                pass

            elif choice == "5":
                Session().clear_session()  # Efface les informations de session
                print("Déconnexion réussie.")
                input("Appuyez sur Entrée pour quitter...")  # Attente avant de quitter
                return None
