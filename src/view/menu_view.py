import requests
from view.abstract_view import AbstractView
from InquirerPy import inquirer


class MenuView(AbstractView):
    def display_info(self):
        print("Que voulez-vous faire ?")

    def make_choice(self):
        choices = [
            {"name": "Effectuer une recherche", "value": "search"},
            {"name": "Consulter mes stations favorites", "value": "favorites"},
            {
                "name": "Modifier/Supprimer mes stations favorites",
                "value": "modify_delete",
            },
            {"name": "Déconnexion", "value": "disconnect"},
        ]

        while True:
            choice = inquirer.select(
                message="Que voulez-vous faire ?", choices=choices
            ).execute()

            if choice == "search":
                # Code pour effectuer une recherche
                pass

            elif choice == "favorites":
                numero = int(input("Entrez le numéro de la liste : "))
                response = requests.get(f"http://127.0.0.1/listesFav/{numero}")
                if response.status_code == 200:
                    data = response.json()
                    print(f"Liste favorite {numero}: {data}")
                else:
                    print(f"Erreur lors de la récupération de la liste {numero}.")

            elif choice == "modify_delete":
                # Code pour modifier ou supprimer les stations favorites
                pass

            elif choice == "disconnect":
                print("Déconnexion réussie.")
                input("Appuyez sur Entrée pour quitter...")
                return None
