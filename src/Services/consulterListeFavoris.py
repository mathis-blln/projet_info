from DAO.consulterListeDAO import ConsulterListeDAO
from Classe import Liste

# Besoin de la classe Session car aucun paramètre va être passé en paramètre


class ConsulterListesFavoris:
    def toutes_les_listes(self, id_user) -> list[Liste]:
        resultat = ConsulterListeDAO().find_all_listes(id_user)
        if len(resultat):
            print("Votre listes sont:")
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


if __name__ == "__main__":
    x = input("Entrer votre id: ")
    ConsulterListesFavoris().toutes_les_listes(x)
