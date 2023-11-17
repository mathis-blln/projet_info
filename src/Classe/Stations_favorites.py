class Station_favorites:
    def __init__(
        self,
        id_utilisateur,
        id_station,
    ):
        """
        Initialise une instance de la classe Station_favorites associant un utilisateur à une station favorite.

        Args:
            id_utilisateur (int): L'identifiant de l'utilisateur qui ajoute la station à ses favoris.
            id_station (int): L'identifiant de la station à ajouter aux favoris de l'utilisateur.
        """
        self._id_utilisateur = id_utilisateur
        self.id_station = id_station

    def __str__(self):
        return f"ID utilisateur: {self._id_utilisateur}, ID station favorite: {self.id_station}"

