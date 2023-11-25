from InquirerPy import prompt
from view.abstract_view import AbstractView
from view.session_view import Session
from Services.authentification import Authentification
from DAO.inscriptionDAO import InscriptionDAO


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
            user_username = answers["nom_utilisateur"]
            user_password = answers["mot_de_passe"]

            auth = Authentification().verifier(user_username, user_password)

            if not auth:
                print("Le nom d'utilisateur ou le mot de passe est incorrect.")
                print("Retour au menu principal...")
                return "EchecConnexion"  # Renvoie "EchecConnexion" en cas d'échec d'authentification

            else:
                session = Session()
                inscriptionDAO = InscriptionDAO()
                user = inscriptionDAO.get_user_by_username(user_username)
                user_id = user[
                    "id_utilisateur"
                ]  # Obtention de l'ID de l'utilisateur à partir du résultat
                print(f"votre identifiant est : {user_id}")
                print("Connexion réussie.")

                import uvicorn
                from fastapi import FastAPI
                import subprocess

                def lancer_api():
                    subprocess.Popen(
                        ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "80"]
                    )

                lancer_api()
                return (
                    None  # Renvoie None pour indiquer que l'authentification a réussi
                )
