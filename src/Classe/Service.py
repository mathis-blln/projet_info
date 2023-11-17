from Classe.Station import Station

class Services:
    def __init__(self, id_service, nom_service):
        """
        Initialise une instance de la classe Services avec un identifiant de service et un nom de service.

        Args:
            id_service (int): L'identifiant du service associé à l'instance.
            nom_service (str): Le nom du service, une description de ce que le service représente.

        Exemple:
            Pour représenter un service de station-service, id_service pourrait être un identifiant unique,
            comme un code, et nom_service pourrait être une chaîne de caractères décrivant le service,
            par exemple "Lavage de voiture" ou "Cafétéria".
        """
        self.id_service = id_service
        self.nom_service = nom_service
    
    def __str__(self):
        return f"ID utilisateur: {self._id_utilisateur}, mot de passe : {self._mot_de_passe}"

         """
        Retourne une représentation sous forme de chaîne de caractères de l'objet Utilisateur.

        Returns:
            str: Une chaîne de caractères représentant l'ID de l'utilisateur et son mot de passe.
        """     
