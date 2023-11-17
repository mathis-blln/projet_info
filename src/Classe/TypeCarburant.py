class TypeCarburant:
    def __init__(self, id_carburant, nom_carburant):
        """
        Initialise une instance de la classe TypeCarburant avec un identifiant de carburant et un nom de carburant.

        Args:
            id_carburant (int): L'identifiant du type de carburant associé à l'instance.
            nom_carburant (str): Le nom du type de carburant (par exemple, "Essence 95", "Diesel", "GPL", etc.).

        Example:
            carburant = TypeCarburant(1, "Essence 95")
        """
        self.id_carburant = id_carburant
        self.nom_carburant = nom_carburant

    def __str__(self):
        return f"ID carburant: {self.id_carburant}, Nom carburant: {self.nom_carburant}"