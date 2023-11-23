class StartView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
                "choices": [
                    "Connexion" "Inscription" "Faire une recherche" "Quitter",
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

            return InscriptionView()

        elif reponse["choix"] == "Faire une recherche":
            from view.recherche_view import RechercheView

            return RechercheView()
