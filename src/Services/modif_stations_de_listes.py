from DAO.stationDAO import StationDAO

# from projet_info.Classe.Utilisateur import Utilisateur


class ModifStationListes:
    """Cette classe gère toutes les actions liées à la modification des listes"""

    def ajouter_station(self, id_liste, id_station):
        station = StationDAO().add_id_station(id_liste, id_station)
        response = {
            "message": "La station a été ajoutée à votre liste : ",
            "id_liste": station[0],
            "id_station": station[1],
        }
        print("-----------------------------------")
        print(response["message"])
        print("-----------------------------------")
        return response

    def remove_station(self, id_liste, id_station):
        station_dao = StationDAO()
        station_dao.remove_id_station(id_liste, id_station)

        response = {
            "message": "La station a été retirée de votre liste : ",
            "id_liste": id_liste,
            "id_station": id_station,
        }
        print("-----------------------------------")
        print(response["message"])
        print("-----------------------------------")
        return response

    def obtenir_id_stations_from_liste(self, id_liste):
        station_dao = StationDAO()
        return station_dao.get_id_stations_from_liste(id_liste)


if __name__ == "__main__":
    ModifStationListes().remove_station(3, "18370001")


# La classe Session pour chaque utilisateur qui se connecte sans
# avoir besoin de demander a chaque fois de faire entrer ses
# identifiant des listes et toute autre chose
