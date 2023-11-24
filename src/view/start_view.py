from InquirerPy import prompt
from view.connexion_view import ConnexionView
from view.inscription_view import InscriptionView

# from view.recherche_view import RechercheView


class StartView:
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Bonjour",
                "choices": [
                    "Connexion",
                    "Inscription",
                    "Faire une recherche",
                    "Quitter",
                ],
            }
        ]

    def make_choice(self):
        while True:
            response = prompt(self.__questions)
            if response["choix"] == "Quitter":
                break
            elif response["choix"] == "Connexion":
                connexion_view = ConnexionView()
                connexion_view.display_info()
                return connexion_view.make_choice()
            elif response["choix"] == "Inscription":
                inscription_view = InscriptionView()
                inscription_view.display_info()
                choice = (
                    inscription_view.make_choice()
                )  # Obtenir le choix de la vue d'inscription
                if (
                    choice == "Connexion"
                ):  # Redirection vers la vue de connexion si l'inscription est réussie
                    connexion_view = ConnexionView()
                    connexion_view.display_info()
                    return connexion_view.make_choice()
            # Gérer d'autres choix ici si nécessaire
            # elif response["choix"] == "Faire une recherche":
            #   recherche_view = RechercheView()
            #  recherche_view.display_info()
            # return recherche_view.make_choice()
