from InquirerPy import prompt
from abstract_view import AbstractView
from session_view import Session
from DAO.inscriptionDAO import InscriptionDAO
<<<<<<< HEAD
from DAO.authentificationDAO import AuthentificationDAO
from view.connexion_view import ConnexionView
=======
>>>>>>> 534726f972cf1a73deee3928a4f090509d351112


class InscriptionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "identifiant",
                "message": "Entrez votre nouvel identifiant",
            },
            {
                "type": "password",
                "name": "mot de passe",
                "message": "Entrez votre mot de passe",
<<<<<<< HEAD
                # "mask": "*",
=======
                "mask": "*",
>>>>>>> 534726f972cf1a73deee3928a4f090509d351112
            },
        ]

    def display_info(self):
<<<<<<< HEAD
        print("-----------------------------------")
        print("Bienvenue ! Veuillez vous inscrire en choisissant un mot de passe.")
        print("Un identifiant vous sera attribué.")
        print("-----------------------------------")
=======
        print(
            "Bienvenue ! Veuillez vous inscrire en choisissant un identifiant et un mot de passe"
        )
>>>>>>> 534726f972cf1a73deee3928a4f090509d351112

    def make_choice(self):
        answers = prompt(self.__questions)
        user_id = answers["identifiant"]
        user_password = answers["mot de passe"]

        # Vérifier si l'identifiant est déjà utilisé dans la base de données
        existing_user = InscriptionDAO().get_user_by_id(user_id)
        if existing_user:
            print("Cet identifiant est déjà utilisé. Veuillez en choisir un autre.")
            return InscriptionView()  # Retourne à la vue d'inscription

        # Si l'identifiant est unique, enregistrer le nouvel utilisateur dans la base de données
        new_user = InscriptionDAO().add_user(user_id, user_password)
        if new_user:
            Session().id_utilisateur = user_id
            Session().mdp_utilisateur = user_password
<<<<<<< HEAD
            print(
                "Votre identifiant est: {}. Il vous sera demandé à chaque connexion.".format(
                    new_user._id_utilisateur
                )
            )
            return ConnexionView()
=======
            from view.start_view import StartView

            return StartView()
>>>>>>> 534726f972cf1a73deee3928a4f090509d351112
        else:
            print("Echec de l'inscription.")
            return InscriptionView()  # Retourne à la vue d'inscription en cas d'échec
