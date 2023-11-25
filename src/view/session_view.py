from singleton_view import Singleton


class Session(metaclass=Singleton):
    def __init__(self):
        """
        Définition des variables que l'on stocke en session
        Le syntaxe
        ref:type = valeur
        permet de donner le type des variables. Utile pour l'autocompletion.
        """
        self.user_name: str = "unknown"

    def clear_session(self):
        # Effacer les données de session
        self.user = None  # Réinitialiser l'utilisateur actuel
