from DAO.db_connection import DBConnection


class AuthentificationDAO:
    """Cette classe gère l'authentification des utilisateurs dans le système.

    >>> Attributs:
        Aucun attribut.
    """

    def verification(self, nom_utilisateur, mdp):
        """Vérifie les informations d'authentification d'un utilisateur.

        Cette méthode interroge la base de données pour vérifier si les
        identifiants fournis correspondent à un utilisateur enregistré.

        >>> Paramètres:
            nom_utilisateur (str): Le nom d'utilisateur de l'utilisateur.
            mdp (str): Le mot de passe de l'utilisateur.

        >>> Returns:
            bool: True si l'authentification réussit, False sinon.
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                       "
                    "  FROM projet.utilisateur                      "
                    " WHERE nom_utilisateur =%(nom_utilisateur)s AND mdp=%(mdp)s   ",
                    {"nom_utilisateur": nom_utilisateur, "mdp": mdp},
                )
                res = cursor.fetchone()

            if res is None:
                return False
            else:
                return True
