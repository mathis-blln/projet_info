from InquirerPy import prompt
from view.abstract_view import AbstractView
from view.session_view import Session
from DAO.inscriptionDAO import InscriptionDAO
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
                # "mask": "*",  # Cache le mot de passe avec les caractères '*'
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
                print("Pour réessayer, tapez 1.")
                print("Pour vous inscrire, tapez 2.")
                print("Pour quitter, tapez 0.")
                choix = input("Votre choix: ")
                if choix == "0":
                    break
                elif choix == "2":
                    inscription_view = InscriptionView()
                    inscription_view.display_info()
                    inscription_view.make_choice()
                else:
                    continue
            else:
                Session().id_utilisateur = user_id
                Session().mdp = user_password
                print("Connexion réussie.")
                menu_view = MenuView()
                MenuView().display_info()
                MenuView().make_choice()
