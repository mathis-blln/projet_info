from InquirerPy import inquirer
from view.abstract_view import AbstractView
from DAO.listeDAO import ListeDAO


class ListesFavoritesView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "nom_liste",
                "message": "Entrez le nom de votre nouvelle liste: ",
            }
        ]

    def display_info(self):
        print("Création d'une nouvelle liste de stations favorites.")

    def make_choice(self):
        answers = inquirer.prompt(self.__questions)
        nom_liste = answers["nom_liste"]
        id_utilisateur = (
            "ID_UTILISATEUR_ACTUEL"  # Remplacez par l'ID de l'utilisateur actuel
        )

        creer_liste = Creerliste()
        creer_liste.ajouter_liste(id_utilisateur, nom_liste)
