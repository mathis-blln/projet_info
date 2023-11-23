from InquirerPy import prompt
from view.abstract_view import AbstractView
from view.session import Session
from projet_info.DAO.InscriptionDAO import InscriptionDAO
from projet_info.Classe.Authentification import Authentification


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
                "message": "Entrez votre mot de passe",
                "mask": "*",  # Cache le mot de passe avec les caractères '*'
            },
        ]

    def display_info(self):
        print("Bonjour, veuillez entrer votre identifiant et votre mot de passe")

    def make_choice(self):
        answers = prompt(self.__questions)
        user_id = answers["identifiant"]
        user_password = answers["mot de passe"]

        # Vérification dans la base de données
        auth_instance = Authentification(
            user_id, user_password
        )  # Crée une instance d'Authentification avec les entrées de l'utilisateur

        user = InscriptionDAO().get_user_by_id(user_id)
        if user and user.compare(user_id, user_password):
            Session().id_utilisateur = user_id
            Session().mdp_utilisateur = user_password
            from view.start_view import StartView

            return StartView()

        print("Identifiant ou mot de passe incorrect")
        input(
            "Appuyez sur Entrée pour retourner à la vue de connexion"
        )  # Attente de l'entrée utilisateur
        return ConnexionView()  # Retourne automatiquement à la vue de connexion
