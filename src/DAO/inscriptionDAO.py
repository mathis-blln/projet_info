from utils.singleton import Singleton
from DAO.db_connection import DBConnection
from Classe.Utilisateur import Utilisateur


class InscriptionDAO(metaclass=Singleton):
    def taille_table(self) -> int:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT COUNT(*)       " "FROM projet.utilisateur             ",
                )
                res = cursor.fetchone()
            if res is not None:
                return int(res["count"])
            else:
                return 0  # Si aucune ligne n'est trouvée, retournez 0

    def add_user(self, nom_utilisateur, mdp):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projet.utilisateur (nom_utilisateur, mdp) "
                    "VALUES (%(nom_utilisateur)s, %(mdp)s) "
                    "RETURNING id_utilisateur",  # Retourne l'id_utilisateur nouvellement généré
                    {
                        "nom_utilisateur": nom_utilisateur,
                        "mdp": mdp,
                    },
                )
                new_user_id = cursor.fetchone()
                if new_user_id is not None:
                    return new_user_id["id_utilisateur"]  # Retourne l'id_utilisateur
                else:
                    return None  # Retourne None en cas d'échec d'insertion

    def get_user_by_id(self, id_utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM projet.utilisateur WHERE id_utilisateur = %(id)s",
                    {"id": int(id_utilisateur)},
                )
                res = cursor.fetchone()
                if res is not None:
                    return Utilisateur(
                        res["id_utilisateur"], res["nom_utilisateur"], res["mdp"]
                    )
                else:
                    return None

    def get_user_by_username(self, username):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM projet.utilisateur WHERE nom_utilisateur = %(username)s",
                    {"username": username},
                )
                return cursor.fetchone()


# if __name__ == "__main__":
#    moi = InscriptionDAO().add_user("Mohamed", "0000")
#    print(
#       "Vos identifiants sont ({},{},{}).".format(
#         moi._id_utilisateur, moi._nom_utilisateur, moi._mot_de_passe
#    )
# )
