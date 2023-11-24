from InquirerPy import prompt
from view.abstract_view import AbstractView
from view.session_view import Session
from DAO.inscriptionDAO import InscriptionDAO
from Services.authentification import Authentification
from view.menu_view import MenuView
from view.connexion_view import ConnexionView


class InscriptionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "identifiant",
                "message": "Entrez votre identifiant",
            },
            {
                "type": "password",
                "name": "mot de passe",
                "message": "Entrez votre mot de passe",
                # "mask": "*",
            },
        ]

    def display_info(self):
        print("-----------------------------------")
        print("Inscription: Entrez votre identifiant et votre mot de passe.")
        print("-----------------------------------")

    def make_choice(self):
        answers = prompt(self.__questions)
        user_id = answers["identifiant"]
        user_password = answers["mot de passe"]

        existing_user = InscriptionDAO().get_user_by_id(user_id)
        if existing_user:
            print("Cet identifiant est déjà utilisé. Veuillez en choisir un autre.")
            return InscriptionView()

        new_user = InscriptionDAO().add_user(user_id, user_password)
        if new_user:
            Session().id_utilisateur = user_id
            Session().mdp_utilisateur = user_password
            Session().id_utilisateur_inscrit = user_id
            print("Inscription réussie.")
            connexion_view = ConnexionView()  # Crée une instance de la vue de connexion
            connexion_view.display_info()  # Affiche les informations de la vue de connexion
            return connexion_view.make_choice()
        else:
            print("Echec de l'inscription.")
            return InscriptionView()
