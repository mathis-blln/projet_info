from DAO.db_connection import DBConnection


class AuthentificationDAO:
    def verification(self, id_utilisateur, mdp):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                       "
                    "  FROM projet.utilisateur                      "
                    " WHERE id_utilisateur =%(id_utilisateur)s AND mdp=%(mdp)s   ",
                    {"id_utilisateur": id_utilisateur, "mdp": mdp},
                )
                res = cursor.fetchone()

            if res is None:
                return False
            else:
                return True
