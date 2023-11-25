from DAO.listeDAO import ListeDAO
from Classe import Liste
from DAO.stationDAO import StationDAO
from Services.service_station import StationsService


# Besoin de la classe Session car aucun paramètre va être passé en paramètre


class ConsulterListesFavoris:
    def consulter_listes(self, id_user) -> list[Liste]:
        resultat = ListeDAO().find_all_listes(id_user)
        self.afficher_listes(resultat)
        return resultat  # Retourne les listes obtenues

    def afficher_listes(self, listes):
        if len(listes):
            print("Vos listes sont:")
            print("-----------------------------------")
            for i, liste in enumerate(listes):
                print(f"Liste {i + 1}: {liste}")
        else:
            print("-----------------------------------")
            print("Aucune liste de favoris trouvée.")
        print("-----------------------------------")

    def creer_nouvelle_liste(self, id_utilisateur: int, nom_liste: str):
        nouvelle_liste = ListeDAO().add_liste(id_utilisateur, nom_liste)
        return nouvelle_liste

    def retirer_liste(self, id_utilisateur, id_liste):
        liste = ListeDAO().remove_liste(id_utilisateur, id_liste)
        return liste

    def information_liste(self, id_liste):
        station = StationDAO()
        id_station = station.get_id_stations_from_liste(id_liste)
        service_station = StationsService()
        informations_stations = service_station.info_stations_preferees(id_station)
        return informations_stations


if __name__ == "__main__":
    consulter = ConsulterListesFavoris()
    consulter.creer_nouvelle_liste(3, "plage")
