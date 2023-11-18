class Liste:
    def __init__(self, id_liste, id_utilisateur, nom_liste):
        self.id_liste = id_liste
        self.id_utilisateur = id_utilisateur
        self.nom_liste = nom_liste

    def __str__(self):
        return f"Liste(id_liste={self.id_liste}, id_utilisateur={self.id_utilisateur}, nom_liste='{self.nom_liste}')"


ma_liste = Liste(id_liste=1, id_utilisateur=42, nom_liste="MaListe")

# Imprimez la représentation sous forme de chaîne de l'objet Liste
print(str(ma_liste))
