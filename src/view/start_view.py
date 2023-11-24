from view.abstract_view import AbstractView
from view.session_view import Session
from InquirerPy import prompt
from view.connexion_view import ConnexionView
from view.inscription_view import InscriptionView


class StartView:
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Bonjour",
                "choices": [
                    "Connexion",
                    "Inscription",
                    "Faire une recherche",
                    "Quitter",
                ],
            }
        ]

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass
        elif reponse["choix"] == "Connexion":
            connexion_view = ConnexionView()
            connexion_view.display_info()
            connexion_view.make_choice()
        elif reponse["choix"] == "Inscription":
            inscription_view = InscriptionView()
            inscription_view.display_info()
            user_choice = inscription_view.make_choice()
            if isinstance(
                user_choice, ConnexionView
            ):  # Vérification si la réponse est de type ConnexionView
                return user_choice  # Si oui, retournez directement la vue de connexion
            return inscription_view
        elif reponse["choix"] == "Faire une recherche":
            pass  # Ajoutez la logique pour la recherche ici
