from InquirerPy import prompt
from view.abstract_view import AbstractView
from view.session_view import Session
from Services.authentification import Authentification
from view.menu_view import MenuView


class ConnexionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "identifiant",
                "message": "Entrez votre identifiant ",
            },
            {
                "type": "password",
                "name": "mot de passe",
                "message": "Entrez votre mot de passe: ",
            },
        ]

    def display_info(self):
        print("Connexion: Entrez votre identifiant et votre mot de passe")

    def make_choice(self):
        while True:
            answers = prompt(self.__questions)
            user_id = answers["identifiant"]
            user_password = answers["mot de passe"]

            auth = Authentification().verifier(user_id, user_password)
            if not auth:
                print("Le mot de passe ne correspond pas à l'identifiant.")
                print("Retour au menu principal...")

                # Retourne une valeur spécifique pour indiquer l'échec de l'authentification
                return "EchecConnexion"

            else:
                Session().id_utilisateur = user_id
                Session().mdp = user_password
                print("Connexion réussie.")
                return "Connexion"
