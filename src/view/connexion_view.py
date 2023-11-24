from InquirerPy import prompt
from view.abstract_view import AbstractView
from view.session_view import Session
from Services.authentification import Authentification


class ConnexionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "identifiant",
                "message": "Entrez votre nom d'utilisateur ",
            },
            {
                "type": "password",
                "name": "mot de passe",
                "message": "Entrez votre mot de passe: ",
            },
        ]

    def display_info(self):
        print("Connexion: Entrez votre nom d'utilisateur et votre mot de passe")

    def make_choice(self):
        while True:
            answers = prompt(self.__questions)
            user_id = answers["identifiant"]
            user_password = answers["mot de passe"]

            # Vérification des identifiants par rapport à ceux stockés lors de l'inscription
            auth = Authentification().verifier(user_id, user_password)
            if not auth:
                print("Le nom d'utilisateur ou le mot de passe est incorrect.")
                print("Retour au menu principal...")
                return "EchecConnexion"

            else:
                # Stockage de l'ID utilisateur dans la session
                Session().id_utilisateur = user_id
                Session().mdp = user_password
                print("Connexion réussie.")
                return "Connexion"
