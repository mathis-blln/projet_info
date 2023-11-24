from DAO.stationDAO import StationDAO

# from projet_info.Classe.Utilisateur import Utilisateur


class ModifStationListes:
    def ajouter_station(self, id_liste, id_station):
        station = StationDAO().add_id_station(id_liste, id_station)
        print("-----------------------------------")
        print(
            "La station avec l'id '{}' a été ajoutée à votre liste dont l'identifiant est '{}'.".format(
                station[1], station[0]
            )
        )
        print("-----------------------------------")

    def remove_station(self, id_liste, id_station):
        station_dao = StationDAO()
        station_dao.remove_id_station(id_liste, id_station)

        # Note : Nous n'avons pas besoin de vérifier si la station a été retirée,
        # car la méthode remove_id_station ne retourne rien.

        print("-----------------------------------")
        print(
            "La station avec l'id '{}' a été retirée de votre liste dont l'identifiant est '{}'.".format(
                id_station, id_liste
            )
        )
        print("-----------------------------------")

    def obtenir_id_stations_from_liste(self, id_liste):
        station_dao = StationDAO()
        return station_dao.get_id_stations_from_liste(id_liste)


if __name__ == "__main__":
    print(ModifStationListes().obtenir_id_stations_from_liste("8"))
# liste de servies

# La classe Session pour chaque utilisateur qui se connecte sans
# avoir besoin de demander a chaque fois de faire entrer ses
# identifiant des listes et toute autre chose
