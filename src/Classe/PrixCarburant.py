from Classe.TypeCarburant import TypeCarburant

class PrixCarburant:
    def __init__(self, id_carburant, id_station, prix):
        """
        Initialise une instance de la classe PrixCarburant avec un identifiant de carburant et son prix.

        Args:
            id_carburant (int): L'identifiant du type de carburant associé à l'instance.
            prix (float): Le prix du carburant en unité monétaire (par exemple, en euros par litre).
        """
        self.id_carburant = id_carburant
        self.id_station = id_station 
        self.prix = prix

        def __str__(self):
        return f"ID utilisateur: {self._id_utilisateur}, mot de passe : {self._mot_de_passe}"

         """
        Retourne une représentation sous forme de chaîne de caractères de l'objet Utilisateur.

        Returns:
            str: Une chaîne de caractères représentant l'ID de l'utilisateur et son mot de passe.
        """     