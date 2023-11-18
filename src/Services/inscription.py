from projet_info.DAO.inscriptionDAO import InscriptionDAO

# from projet_info.Classe.Utilisateur import Utilisateur


# on peut ajouter des fonctions comme changer mdp
class Inscription:
    def inscrire(self, nom_utilsateur, mdp):
        inscrit = InscriptionDAO().add_user(nom_utilsateur, mdp)
        print("-----------------------------------")
        print(
            "Bienvenu.\nVos identifiants\nID: {}\nNom: {}\nPassword: {}.".format(
                inscrit._id_utilisateur, inscrit._nom_utilisateur, inscrit._mot_de_passe
            )
        )
        print("-----------------------------------")


if __name__ == "__main__":
    Inscription().inscrire("Utilisateur", "Mot de passe")
