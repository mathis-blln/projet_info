from DAO.db_connection import DBConnection


class StationDAO:
    def add_id_station(self, id_liste, id_stations):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projet.contenu_liste (id_liste, id_stations)"
                    "VALUES (%(id_liste)s, %(id_stations)s)"
                    "RETURNING id_liste, id_stations",
                    {"id_liste": int(id_liste), "id_stations": id_stations},
                )
                res = cursor.fetchone()
                return [res["id_liste"], res["id_stations"]]

    def remove_id_station(self, id_liste, id_stations):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM projet.contenu_liste "
                    "WHERE id_liste = %(id_liste)s AND id_stations = %(id_stations)s",
                    {"id_liste": int(id_liste), "id_stations": id_stations},
                )
                connection.commit()

    def get_id_stations_from_liste(self, id_liste):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_stations FROM projet.contenu_liste WHERE id_liste = %(id_liste)s",
                    {"id_liste": int(id_liste)},
                )
                result = cursor.fetchall()
                return [row["id_stations"] for row in result]
