from view.abstract_view import AbstractView
from InquirerPy import prompt


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
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Connexion":
            from view.connexion_view import ConnexionView

            return ConnexionView()

        elif reponse["choix"] == "Inscription":
            from view.inscription_view import InscriptionView

            inscription_view = InscriptionView()
            inscription_view.display_info()
            return inscription_view.make_choice()

        elif reponse["choix"] == "Faire une recherche":
            from view.recherche_view import RechercheView

<<<<<<< HEAD
            return CreatePokemonView()
=======
            return RechercheView()
>>>>>>> ee9645d046912deac142db99fa25d3cd86cf67e2
