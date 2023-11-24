from DAO.authentificationDAO import AuthentificationDAO
from DAO.db_connection import DBConnection


class Application:
    def __init__(self):
        self.current_view = None

    def afficher_menu_principal(self):
        print("1. Se connecter")
        print("2. Créer un compte")
        print("3. Quitter")

    def afficher_connexion(self):
        print("Saisissez votre identifiant")
        id_user = input()
        print("Saisissez votre mot de passe")
        mdp = input()
        if verification(self, id_user, mdp):
            self.afficher_profil
        else:
            print("Identifiant ou mot de passe incorrect")
            self.afficher_menu_principal

    def afficher_vue2(self):
        print("Vous êtes dans la Vue 2.")
        input("Appuyez sur Entrée pour revenir au menu principal.")

    def afficher_profil(self):
        print

    def executer(self):
        while True:
            self.afficher_menu_principal()
            choix = input("Choisissez une option : ")

            if choix == "1":
                self.afficher_vue1()
            elif choix == "2":
                self.afficher_vue2()
            elif choix == "3":
                print("Au revoir !")
                break
            else:
                print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    app = Application()
    app.executer()
