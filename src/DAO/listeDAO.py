from projet_info.DAO.db_connection import DBConnection
from projet_info.Classe.Liste import Liste
from typing import Optional

class ListeDAO:

    def find_all_listes(self, id_user):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
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

    def taille_table(self, id_user) -> int:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT COUNT(*)       "
                    "FROM projet.listes             ",
                )
                res = cursor.fetchone()

            if res is not None:
                return int(res["count"])
            else:
                return 0  # Si aucune liste n'est trouvée, retournez 0

    def add_liste(self, id_user, nom_liste) -> Liste:
        id_liste = self.taille_table(id_user) + 1
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projet.listes (id_liste, id_utilisateur, nom_liste)"
                    "VALUES                                                         "
                    "(%(id_liste)s, %(id_utilisateur)s, %(nom_liste)s)              "
                    "RETURNING id_liste, id_utilisateur, nom_liste                  ",
                    {
                        "id_liste": id_liste,
                        "id_utilisateur": id_user,
                        "nom_liste": nom_liste
                    },
                )
                res = cursor.fetchone()
                element = Liste(res["id_liste"], res["id_utilisateur"], res["nom_liste"])
                return element

    def remove_liste(self, id_user, id_liste) -> Optional[bool]:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM projet.listes WHERE id_utilisateur = %(id_utilisateur)s AND id_liste = %(id_liste)s",
                    {
                        "id_utilisateur": id_user,
                        "id_liste": id_liste
                    },
                )
                # Vous pouvez vérifier si la suppression a réussi en vérifiant le nombre de lignes affectées.
                if cursor.rowcount > 0:
                    return True  # La liste a été supprimée avec succès
                else:
                    return False  # La liste n'a pas été trouvée ou n'a pas été supprimée
