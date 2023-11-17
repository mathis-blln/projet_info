from projet_info.utils.singleton import Singleton
from projet_info.DAO.db_connection import DBConnection
from projet_info.Classe.Utilisateur import Utilisateur


class InscriptionDAO(metaclass=Singleton):
    def taille_table(self) -> int:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT COUNT(*)       "
                    "FROM projet.utilisateur             ",
                )
                res = cursor.fetchone()          
            if res is not None:
                return int(res["count"])
            else:
                return 0  # Si aucune ligne n'est trouvée, retournez 0

    def add_user(self, nom_utilisateur, mdp) -> Utilisateur:
        id_utilisateur = self.taille_table() + 1
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projet.utilisateur (id_utilisateur, nom_utilisateur, mdp)"
                    "VALUES                                                   "
                    "(%(id_utilisateur)s, %(nom_utilisateur)s, %(mdp)s)      "
                    "RETURNING id_utilisateur, nom_utilisateur, mdp           ",
                    {
                        "id_utilisateur": id_utilisateur,
                        "nom_utilisateur": nom_utilisateur,
                        "mdp": mdp,
                    },
                )
                res = cursor.fetchone()
                if res is not None:
                    user = Utilisateur(res["id_utilisateur"], res["nom_utilisateur"], res["mdp"]) 
                    return user
                else:
                    print("Echec d'inscription.")


if __name__ == "__main__":
    moi = InscriptionDAO().add_user("Mohamed", "0000")
    print("Vos identifiants sont ({},{},{}).".format(moi._id_utilisateur, moi._nom_utilisateur, moi._mot_de_passe))
