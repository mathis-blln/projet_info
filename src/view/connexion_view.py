from InquirerPy import prompt
from view.abstract_view import AbstractView
from view.session_view import Session
from Services.authentification import Authentification


class ConnexionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "nom_utilisateur",
                "message": "Entrez votre nom d'utilisateur ",
            },
            {
                "type": "password",
                "name": "mot_de_passe",
                "message": "Entrez votre mot de passe: ",
            },
        ]

    def display_info(self):
        print("Connexion: Entrez votre nom d'utilisateur et votre mot de passe")

    def make_choice(self):
        while True:
            answers = prompt(self.__questions)
            user_id = answers["nom_utilisateur"]
            user_password = answers["mot_de_passe"]

            auth = Authentification().verifier(user_id, user_password)

            if not auth:
                print("Le nom d'utilisateur ou le mot de passe est incorrect.")
                print("Retour au menu principal...")
                return "EchecConnexion"  # Renvoie "EchecConnexion" en cas d'échec d'authentification

            else:
                # Si l'authentification réussit, stockez l'ID utilisateur dans la session
                Session().id_utilisateur = user_id
                Session().mdp = user_password
                print("Connexion réussie.")
                return (
                    None  # Renvoie None pour indiquer que l'authentification a réussi
                )
