import requests
from view.abstract_view import AbstractView
from InquirerPy import inquirer
from view.session_view import Session


class MenuView(AbstractView):
    def display_info(self):
        print("Que voulez-vous faire ?")

    def make_choice(self):
        choices = [
            {"name": "Accéder à mon compte", "value": "search"},
            {"name": "Déconnexion", "value": "disconnect"},
        ]

        while True:
            choice = inquirer.select(
                message="Que voulez-vous faire ?", choices=choices
            ).execute()

            if choice == "search":
                print("ouvrez le lien suivant")
                print("http://127.0.0.1/docs")
            elif choice == "disconnect":
                Session().clear_session()  # Nettoyer la session

                print("Déconnexion réussie.")
                return None  # Quitter l'interface

            input("Appuyez sur Entrée pour quitter...")
            return None
