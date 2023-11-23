import sys

sys.path.insert(0, "\\filer-eleves2\id2315\projet_info\projet_info")
from projet_info.DAO.InscriptionDAO import InscriptionDAO

from InquirerPy import inquirer
from abstract_view import AbstractView
from session_view import Session
from projet_info.DAO.InscriptionDAO import InscriptionDAO
from projet_info.DAO.MenuDAO import (
    MenuDAO,
)  # Créez votre propre DAO pour gérer les fonctionnalités du menu


class MenuView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "select",
                "name": "choice",
                "message": "Que voulez-vous faire ?",
                "choices": [
                    {"name": "Effectuer une recherche"},
                    {"name": "Consulter mes stations favorites"},
                    {"name": "Modifier/Supprimer mes stations favorites"},
                    {"name": "Déconnexion"},
                ],
            }
        ]

    def display_info(self):
        print("Bienvenue dans le menu !")

    def make_choice(self):
        while True:
            answers = inquirer.prompt(self.__questions)
            choice = answers["choice"]

            if choice == "Effectuer une recherche":
                # Ajoutez le code pour l'option "Effectuer une recherche"
                pass
            elif choice == "Consulter mes stations favorites":
                # Ajoutez le code pour l'option "Consulter mes stations favorites"
                pass
            elif choice == "Modifier/Supprimer mes stations favorites":
                # Ajoutez le code pour l'option "Modifier/Supprimer mes stations favorites"
                pass
            elif choice == "Déconnexion":
                Session().clear_session()  # Efface les informations de session
                from view.connexion_view import ConnexionView

                return ConnexionView()  # Retourne à la vue de connexion

            input(
                "Appuyez sur Entrée pour revenir au menu"
            )  # Attente de l'entrée utilisateur pour revenir au menu principal
