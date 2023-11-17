from projet_info.DAO.db_connection import DBConnection
from projet_info.Classe.Liste import Liste



class ConsulterListeDAO:
    def find_all_listes(self, id_user):  # La fonction taille_table est importante 
        with DBConnection().connection as connection:  # pour affecter à chaque nouveau
            with connection.cursor() as cursor:  # objet un "id" différent
                cursor.execute(
                    "SELECT id_utilisateur, id_liste, nom_liste         "
                    "FROM projet.listes                                 "
                    "WHERE id_utilisateur = %(id_user)s                 ",
                    {"id_user": id_user},
                )
                res = cursor.fetchall()

            listes = []

            if res is not None:
                for row in res:
                    arg1 = row["id_liste"]
                    arg2 = row["id_utilisateur"]
                    arg3 = row["nom_liste"]
                    element = Liste(arg1, arg2, arg3)
                    listes.append(element)

            return listes
