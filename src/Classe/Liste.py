class Liste:
    def __init__(self, id_liste, id_utilisateur, nom_liste):
        self.id_liste = id_liste
        self.id_utilisateur = id_utilisateur
        self.nom_liste = nom_liste

    def __str__(self):
        return f"Liste(id_liste={self.id_liste}, id_utilisateur={self.id_utilisateur}, nom_liste='{self.nom_liste}')"
