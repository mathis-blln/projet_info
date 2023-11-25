import requests
from view.abstract_view import AbstractView
from view.session_view import Session
from DAO.inscriptionDAO import InscriptionDAO


class MenuView(AbstractView):
    def display_info(self):
        print("Que voulez-vous faire ?")

    def make_choice(self):
        while True:
            print("1. Effectuer une recherche")
            print("2. Consulter mes stations favorites")
            print("3. Modifier/Supprimer mes stations favorites")
            print("4. Créer une liste de stations favorites")
            print("5. Déconnexion")

            choice = input("Votre choix : ")

            if choice == "1":
                response = requests.get("http://127.0.0.1/listesFav/")
                if response.status_code == 200:
                    data = response.json()
                    print("Listes favorites disponibles:")
                    for key, value in data.items():
                        print(f"{key}: {value}")
                else:
                    print("Erreur lors de la récupération des listes favorites.")

            elif choice == "2":
                numero = int(input("Entrez le numéro de la liste: "))
                response = requests.get(f"http://127.0.0.1/listesFav/{numero}")
                if response.status_code == 200:
                    data = response.json()
                    print(f"Liste favorite {numero}: {data}")
                else:
                    print(f"Erreur lors de la récupération de la liste {numero}.")

            elif choice == "3":
                pass  # Ajoutez le code pour "Modifier/Supprimer mes stations favorites"

            elif choice == "4":
                pass  # Ajoutez le code pour "Créer une liste de stations favorites"

            elif choice == "5":
                Session().clear_session()
                print("Déconnexion réussie.")
                input("Appuyez sur Entrée pour quitter...")
                return None
