import requests
from view.abstract_view import AbstractView
from view.session_view import Session
from DAO.inscriptionDAO import InscriptionDAO


class MenuView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choice",
                "message": "Que voulez-vous faire ?",
                "choices": [
                    "Effectuer une recherche",
                    "Consulter mes stations favorites",
                    "Modifier/Supprimer mes stations favorites",
                    "Déconnexion",
                    # {"name": "Effectuer une recherche", "value": 1},
                    # {"name": "Consulter mes stations favorites", "value": 2},
                    # {"name": "Modifier/Supprimer mes stations favorites", "value": 3},
                    # {"name": "Créer une liste de stations favorites", "value": 4},
                    # {"name": "Déconnexion", "value": 5},
                ],
            },
        ]

    def display_info(self):
        print("Que voulez-vous faire ?")

    def make_choice(self):
        while True:
            answers = prompt(self.__questions)
            choice = answers["choice"]

            if choice == "Effectuer une recherche":
                # Appel à l'API pour obtenir toutes les listes favorites
                response = requests.get("http://127.0.0.1/listesFav/")
                if response.status_code == 200:
                    data = response.json()
                    print("Listes favorites disponibles:")
                    for key, value in data.items():
                        print(f"{key}: {value}")
                else:
                    print("Erreur lors de la récupération des listes favorites.")

            elif choice == "Consulter mes stations favorites":
                # Appel à l'API pour obtenir une liste spécifique
                numero = int(input("Entrez le numéro de la liste: "))
                response = requests.get(f"http://127.0.0.1/listesFav/{numero}")
                if response.status_code == 200:
                    data = response.json()
                    print(f"Liste favorite {numero}: {data}")
                else:
                    print(f"Erreur lors de la récupération de la liste {numero}.")

            elif choice == "Modifier/Supprimer mes stations favorites":
                # Ajoutez le code pour l'option "Modifier/Supprimer mes stations favorites"
                pass

            # elif choice == "4":
            #     pass

            elif choice == "Déconnexion":
                # Session().clear_session()  # Efface les informations de session
                print("Déconnexion réussie.")
                input("Appuyez sur Entrée pour quitter...")
                return None
