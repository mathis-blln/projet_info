from InquirerPy import prompt
from view.abstract_view import AbstractView
from view.session_view import Session
from DAO.inscriptionDAO import InscriptionDAO
from Services.authentification import Authentification
from view.inscription_view import InscriptionView
from view.menu_view import MenuView


class ConnexionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "identifiant",
                "message": "Entrez votre identifiant: ",
            },
            {
                "type": "password",
                "name": "mot de passe",
                "message": "Entrez votre mot de passe: ",
                # "mask": "*",  # Cache le mot de passe avec les caractères '*'
            },
        ]

    def display_info(self):
        print("Bonjour, veuillez entrer votre identifiant et votre mot de passe.")

    def make_choice(self):
        detecte = 0
        while not detecte:
            answers = prompt(self.__questions)
            user_id = answers["identifiant"]
            user_password = answers["mot de passe"]
            Session().id_utilisateur = user_id
            Session().mdp = user_password
            # Vérification dans la base de données
            auth = Authentification().verifier(user_id, user_password)
            # Crée une instance d'Authentification avec les entrées de l'utilisateur
            if not auth:
                # user = InscriptionDAO().get_user_by_id(user_id)
                # if user and user.compare(user_id, user_password):
                #     Session().id_utilisateur = user_id
                #     Session().mdp_utilisateur = user_password
                #     from view.start_view import StartView

                #     return StartView()
                print("-----------------------------------")
                print(
                    "Le mot de passe rentré ne correspond pas à l'identifiant choisi."
                )
                print("-----------------------------------")
                print("Pour réessayer, tapez 1.")
                print("Pour s'inscrire, tapez 2.")
                print("Pour quitter, tapez 0.")
                print("-----------------------------------")
                choix = input("Votre choix: ")
                if choix == "0":
                    break
                elif choix == "2":
                    InscriptionView().display_info()
                    InscriptionView().make_choice()
                    print("-----------------------------------")
                else:
                    print("-----------------------------------")
                    continue

            else:
                detecte = 1
                print("-----------------------------------")
                print("Connexion réussite.")
                print("-----------------------------------")
                MenuView().display_info()
                MenuView().make_choice()

            # input(
            #     "Appuyez sur Entrée pour retourner à la vue de connexion"
            # )  # Attente de l'entrée utilisateur
            # return ConnexionView()  # Retourne automatiquement à la vue de connexion
