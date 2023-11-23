from DAO.listeDAO import ListeDAO
from Classe import Liste

# Besoin de la classe Session car aucun paramètre va être passé en paramètre


class ConsulterListesFavoris:
    def consulter_listes(self, id_user) -> list[Liste]:
        resultat = ListeDAO().find_all_listes(id_user)
        if len(resultat):
            print("Vos listes sont:")
            print("-----------------------------------")
            for i in range(len(resultat)):
                print(
                    "Liste {}: (id liste: {}, nom liste: {})".format(
                        i + 1, resultat[i].id_liste, resultat[i].nom_liste
                    )
                )
                # print(resultat[i]["id_liste"])
        else:
            print("-----------------------------------")
            print("Aucune liste de favoris trouvée.")

        print("-----------------------------------")
        return resultat

    def consulter_listes2(self, id_user) -> list[Liste]:
        resultat = ListeDAO().find_all_listes(id_user)
        self.afficher_listes(resultat)
        return resultat  # Retourne les listes obtenues

    def afficher_listes(self, listes):
        if len(listes):
            print("Vos listes sont:")
            print("-----------------------------------")
            for i, liste in enumerate(listes):
                print(f"Liste {i + 1}: {liste}")
        else:
            print("-----------------------------------")
            print("Aucune liste de favoris trouvée.")
        print("-----------------------------------")


if __name__ == "__main__":
    x = input("Entrer votre id: ")
    y = ConsulterListesFavoris().consulter_listes2(x)
