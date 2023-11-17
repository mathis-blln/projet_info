class Utilisateur:
    def __init__(
        self,
        id_utilisateur,
        nom_utilisateur,
        mot_de_passe,
    ):
        """
        Initialise une instance de la classe Utilisateur avec un identifiant d'utilisateur, un nom d'utilisateur et un mot de passe.

        Args:
            id_utilisateur (int): L'identifiant unique de l'utilisateur associé à l'instance.
            nom_utilisateur (str): Le nom d'utilisateur ou le pseudonyme de l'utilisateur.
            mot_de_passe (str): Le mot de passe de l'utilisateur pour l'authentification.

        Attributes:
            _id_utilisateur (int): L'identifiant unique de l'utilisateur.
            _nom_utilisateur (str): Le nom d'utilisateur ou pseudonyme.
            _mot_de_passe (str): Le mot de passe de l'utilisateur.

        Example:
            utilisateur = Utilisateur(1, "john_doe", "mot_de_passe_secure")
        """
        self._id_utilisateur = id_utilisateur
        self._nom_utilisateur = nom_utilisateur
        self._mot_de_passe = mot_de_passe

    def __str__(self):
        return f"ID utilisateur: {self._id_utilisateur}, Nom utilisateur: {self._nom_utilisateur}"