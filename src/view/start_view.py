from view.abstract_view import AbstractView
from view.session_view import Session
from InquirerPy import prompt
from view.connexion_view import ConnexionView


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
            from view.inscription_view import InscriptionView

            inscription_view = InscriptionView()
            inscription_view.display_info()
            result = inscription_view.make_choice()
            # Vérifie si l'inscription a été réussie et renvoie la vue de connexion si c'est le cas
            if result == "Inscription réussie !":
                return ConnexionView()

        elif reponse["choix"] == "Faire une recherche":
            from view.recherche_view import RechercheView

            return RechercheView()
