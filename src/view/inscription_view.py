from InquirerPy import prompt
from view.abstract_view import AbstractView
from view.session_view import Session
from DAO.inscriptionDAO import InscriptionDAO


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
                continue  # Retourner à la saisie du nom d'utilisateur

            new_user_id = InscriptionDAO().add_user(user_username, user_password)
            if (
                new_user_id
            ):  # Supposons que add_user() retourne l'ID nouvellement généré
                session = Session()  # Instanciation de la session en tant qu'objet
                session.id_utilisateur = (
                    new_user_id  # Stockage de l'ID utilisateur dans la session
                )
                session.nom_utilisateur = user_username
                session.mdp_utilisateur = user_password
                print("Inscription réussie.")
                return "Connexion"
            else:
                print("Echec de l'inscription.")
                return "Inscription"
