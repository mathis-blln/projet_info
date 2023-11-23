from InquirerPy import prompt
from view.abstract_view import AbstractView
from view.session_view import Session
from DAO.inscriptionDAO import InscriptionDAO
from DAO.authentificationDAO import AuthentificationDAO
from view.connexion_view import ConnexionView


class InscriptionView(AbstractView):
    def __init__(self):
        self.__questions = [
            # {
            #     "type": "input",
            #     "name": "identifiant",
            #     "message": "Entrez votre nouvel identifiant: ",
            # },
            {
                "type": "input",
                "name": "Nom Complet",
                "message": "Entrez votre nom: ",
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
        print("Bienvenue ! Veuillez vous inscrire en choisissant un mot de passe.")
        print("Un identifiant vous sera attribué.")
        print("-----------------------------------")

    def make_choice(self):
        answers = prompt(self.__questions)
        # user_id = answers["identifiant"]
        user_name = answers["Nom Complet"]
        user_password = answers["mot de passe"]

        # # Vérifier si l'identifiant est déjà utilisé dans la base de données
        # existing_user = AuthentificationDAO().verification(user_id, user_password)
        # if existing_user:
        #     print("Cet identifiant est déjà utilisé. Veuillez en choisir un autre.")
        #     return InscriptionView()  # Retourne à la vue d'inscription

        # Si l'identifiant est unique, enregistrer le nouvel utilisateur dans la base de données
        new_user = InscriptionDAO().add_user(user_name, user_password)
        if new_user:
            Session().id_utilisateur = new_user._id_utilisateur
            Session().mdp_utilisateur = user_password
            print(
                "Votre identifiant est: {}. Il vous sera demandé à chaque connexion.".format(
                    new_user._id_utilisateur
                )
            )
            return ConnexionView()
        else:
            print("Echec de l'inscription.")
            InscriptionView()  # Retourne à la vue d'inscription en cas d'échec
