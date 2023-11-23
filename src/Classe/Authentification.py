class Authentification:
    def __init__(self, id_utilisateur, mot_de_passe):
        """
        Initialise une instance de la classe Authentification avec un nom d'utilisateur et un mot de passe.

        Args:
            id_utilisateur (str): Le nom d'utilisateur associé à l'instance.
            mot_de_passe (str): Le mot de passe associé à l'instance.
        """
        self._id_utilisateur = id_utilisateur
        self._mot_de_passe = mot_de_passe

    def __str__(self):
        return f"ID utilisateur: {self._id_utilisateur}, mot de passe : {self._mot_de_passe}"
        """
        Retourne une représentation sous forme de chaîne de caractères de l'objet Utilisateur.

        Returns:
            str: Une chaîne de caractères représentant l'ID de l'utilisateur et son mot de passe.
        """

    def compare(self, id_utilisateur, mot_de_passe):
        """
        Compare les noms d'utilisateur et les mots de passe pour vérifier l'authentification.

        Args:
            id_utilisateur (str): Le nom d'utilisateur à vérifier.
            mot_de_passe (str): Le mot de passe à vérifier.

        Returns:
            bool: True si les identifiants sont valides, False sinon.
        """
        if (
            self._id_utilisateur == id_utilisateur
            and self._mot_de_passe == mot_de_passe
        ):
            return True
        else:
            return False


# pas utilisée non plus
