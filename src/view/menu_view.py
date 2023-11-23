<<<<<<< HEAD
from InquirerPy import prompt

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

=======
import sys

sys.path.insert(0, "\\filer-eleves2\id2315\projet_info\projet_info")
from DAO.InscriptionDAO import InscriptionDAO

from InquirerPy import inquirer
from abstract_view import AbstractView
from session_view import Session
from DAO.InscriptionDAO import InscriptionDAO
from DAO.MenuDAO import (
    MenuDAO,
)  # Créez votre propre DAO pour gérer les fonctionnalités du menu

>>>>>>> ee9645d046912deac142db99fa25d3cd86cf67e2

class MenuView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choice",
                "message": "Que voulez-vous faire ?\n-----------------------------------",
                "choices": [
<<<<<<< HEAD
                    # "Effectuer une recherche",
                    # "Consulter mes stations favorites",
                    # "Modifier/Supprimer mes stations favorites",
                    # "Déconnexion",
                    {"name": "Effectuer une recherche", "value": "1"},
                    {"name": "Consulter mes stations favorites", "value": "2"},
                    {"name": "Modifier/Supprimer mes stations favorites", "value": "3"},
                    {"name": "Déconnexion", "value": "4"},
                ],
            },
=======
                    {"name": "Effectuer une recherche"},
                    {"name": "Consulter mes stations favorites"},
                    {"name": "Modifier/Supprimer mes stations favorites"},
                    {"name": "Déconnexion"},
                ],
            }
>>>>>>> ee9645d046912deac142db99fa25d3cd86cf67e2
        ]

    def display_info(self):
        print("Bienvenue dans le menu !")
        print("-----------------------------------")

    def make_choice(self):
        while True:
            answers = prompt(self.__questions)
            choice = answers["choice"]

            if choice == "1":
                # Ajoutez le code pour l'option "Effectuer une recherche"
                pass
            elif choice == "2":
                # Ajoutez le code pour l'option "Consulter mes stations favorites"
                pass
            elif choice == "3":
                # Ajoutez le code pour l'option "Modifier/Supprimer mes stations favorites"
                pass
            elif choice == "4":
                Session().clear_session()  # Efface les informations de session
                from view.connexion_view import ConnexionView

                return ConnexionView()  # Retourne à la vue de connexion

            input(
                "Appuyez sur Entrée pour revenir au menu"
            )  # Attente de l'entrée utilisateur pour revenir au menu principal
