from Classe.Coordonnees import Coordonnees

class Station:
    def __init__(
        self,
        id_station,
        longitude,
        latitude,
        ville,
        adresse,
        type_carburant,
        prix_carburant,
        coordonnees,
    ):
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
        self.longitude = longitude
        self.latitude = latitude
        self.ville = ville
        self.adresse = adresse
        self.type_carburant = type_carburant
        self.prix_carburant = prix_carburant
        self.coordonnees = coordonnees
        self.services = []

    def __str__(self):
        return f"ID Station: {self.id_station}\n" \
               f"Coordonnées: {self.coordonnees}\n" \
               f"Ville: {self.ville}\n" \
               f"Adresse: {self.adresse}\n" \
               f"Type de Carburant: {self.type_carburant}\n" \
               f"Prix du Carburant: {self.prix_carburant} euros par litre\n" \
               f"Services: {', '.join(self.services)}"  # Affiche les services séparés par une virgule

    def ajouter_service(self, nom_service):
        """
        Ajoute un service à la liste des services disponibles à la station.

        Args:
            nom_service (str): Le nom du service à ajouter.
        """
        self.services.append(nom_service)

    def service_disponible(self, nom_service: str) -> bool:
        """
        Vérifie si un service spécifique est disponible à la station.

        Args:
            nom_service (str): Le nom du service à vérifier.

        Returns:
            bool: True si le service est disponible à la station, False sinon.
        """
        return nom_service in self.services

    def rechercher_par_preference(self):
        """
        Méthode permettant de rechercher des stations en fonction des préférences.

        Cette méthode peut être utilisée pour rechercher des stations en fonction de critères spécifiques, tels que le type de carburant, le prix du carburant, la disponibilité de certains services, etc.
        Elle peut renvoyer une liste de stations qui correspondent aux préférences spécifiées.
        """
        pass
