class Horaires:
    def __init__(self, ouverture, fermeture):
        """
        Initialise une instance de la classe Horaires avec des horaires d'ouverture et de fermeture.

        Args:
            ouverture (str): L'heure d'ouverture au format HH:MM (par exemple, "08:00").
            fermeture (str): L'heure de fermeture au format HH:MM (par exemple, "18:00").
        """
        self.ouverture = ouverture
        self.fermeture = fermeture
   
    def __str__(self):
        return f"ID utilisateur: {self._id_utilisateur}, mot de passe : {self._mot_de_passe}"

         """
        Retourne une représentation sous forme de chaîne de caractères de l'objet Utilisateur.

        Returns:
            str: Une chaîne de caractères représentant l'ID de l'utilisateur et son mot de passe.
        """     