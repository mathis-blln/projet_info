from Classe.Coordonnees import Coordonnees


class Station:
    def __init__(self, id_station, cp, ville, adresse, coordonnees, prix_carburant):
        """
        Initialise une instance de la classe Station représentant une station-service.

        Args:
            id_station (int): L'identifiant unique de la station.
            longitude (float): La longitude géographique de la station.
            latitude (float): La latitude géographique de la station.
            ville (str): Le nom de la ville où se trouve la station.
            adresse (str): L'adresse précise de la station.
            type_carburant (str): Le type de carburant disponible à la station.
            prix_carburant (float): Le prix du carburant en unité monétaire (par exemple, en euros par litre).
            coordonnees (Coordonnees): Un objet Coordonnees représentant les coordonnées géographiques de la station.

        Attributes:
            services (list): Une liste des services disponibles à la station.

        Methods:
            ajouter_service(nom_service): Ajoute un service à la liste des services disponibles.
            service_disponible(nom_service: str) -> bool: Vérifie si un service spécifique est disponible à la station.
            rechercher_par_preference(): Méthode permettant de rechercher des stations en fonction des préférences.

        Example:
            station = Station(1, 2.345, 51.789, "Villeville", "123 Rue de la Station",
                              "Essence 95", 1.45, Coordonnees(51.789, 2.345))
        """
        self.id_station = id_station
        self.cp = cp
        self.ville = ville
        self.adresse = adresse
        self.coordonnees = coordonnees
        self.prix_carburant = prix_carburant

    def __str__(self):
        return (
            f"ID Station: {self.id_station}\n"
            f"Coordonnées: {self.coordonnees}\n"
            f"Ville: {self.ville}\n"
            f"Adresse: {self.adresse}\n"
            f"Prix carburant choisi : {self.prix_carburant}\n"
        )
