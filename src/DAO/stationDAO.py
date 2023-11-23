from DAO.db_connection import DBConnection


class StationDAO:
    def add_id_station(self, id_liste, id_stations):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projet.contenu_liste (id_liste, id_stations)"
                    "VALUES (%(id_liste)s, %(id_stations)s)"
                    "RETURNING id_liste, id_stations",
                    {"id_liste": id_liste, "id_stations": id_stations},
                )
                res = cursor.fetchone()
                return [res["id_liste"], res["id_stations"]]

    def get_id_stations_for_liste(self, id_liste):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_stations FROM projet.contenu_liste WHERE id_liste = %(id_liste)s",
                    {"id_liste": id_liste},
                )
                result = cursor.fetchall()
                return [row["id_stations"] for row in result]

    def remove_id_station(self, id_liste, id_stations):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM projet.contenu_liste "
                    "WHERE id_liste = %(id_liste)s AND id_stations = %(id_stations)s",
                    {"id_liste": id_liste, "id_stations": id_stations},
                )

    # def creer_station(self, id_station, adresse, ville):
    #     with DBConnection().connection as connection:
    #         with connection.cursor() as cursor:
    #             cursor.execute(
    #                 "INSERT INTO projet.stations (id_stations, adresse, ville)"
    #                 "VALUES                                                  "
    #                 "(%(id_stations)s, %(adresse)s, %(ville)s)              ",
    #                 # "RETURNING id_station, adresse, ville                 ",
    #                 {
    #                     "id_stations": id_station,
    #                     "adresse": adresse,
    #                     "ville": ville
    #                 },
    #             )
    # res = cursor.fetchone()