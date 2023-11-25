from InquirerPy import prompt
from view.abstract_view import AbstractView
from DAO.inscriptionDAO import InscriptionDAO
from Classe.Utilisateur import Utilisateur
from view.connexion_view import (
    ConnexionView,
)  # Importez la vue ConnexionView appropriée


class InscriptionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "nom_utilisateur",
                "message": "Entrez votre nom d'utilisateur",
            },
            {
                "type": "password",
                "name": "mot_de_passe",
                "message": "Entrez votre mot de passe",
            },
        ]

    def display_info(self):
        print("-----------------------------------")
        print("Inscription: Entrez votre nom d'utilisateur et votre mot de passe.")
        print("-----------------------------------")

    def make_choice(self):
        while True:
            answers = prompt(self.__questions)
            user_username = answers["nom_utilisateur"]
            user_password = answers["mot_de_passe"]

            existing_user = InscriptionDAO().get_user_by_username(user_username)
            if existing_user:
                print(
                    "Ce nom d'utilisateur est déjà utilisé. Veuillez en choisir un autre."
                )
                return "EchecInscription"  # Modifier le retour en cas d'échec

            new_user_id = InscriptionDAO().add_user(user_username, user_password)
            if new_user_id:
                session = Utilisateur(new_user_id, user_username, user_password)
                print("Inscription réussie.")
                print(new_user_id)
                return "Connexion"  # Redirige vers la vue Connexion après l'inscription
            else:
                print("Echec de l'inscription.")
                return "EchecInscription"
