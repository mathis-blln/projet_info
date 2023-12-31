from DAO.inscriptionDAO import InscriptionDAO

# from projet_info.Classe.Utilisateur import Utilisateur


# on peut ajouter des fonctions comme changer mdp, ou le hashage
class Inscription:
    def inscrire(self, nom_utilsateur, mdp):
        inscrit = InscriptionDAO().add_user(nom_utilsateur, mdp)
        print("-----------------------------------")
        print(
            "Bienvenue.\nVos identifiants\nID: {}\nNom: {}\nPassword: {}.".format(
                inscrit._id_utilisateur, inscrit._nom_utilisateur, inscrit._mot_de_passe
            )
        )
        print("-----------------------------------")


if __name__ == "__main__":
    Inscription().inscrire("mathis9", "pom0o0o")
