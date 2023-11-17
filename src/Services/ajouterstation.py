from projet_info.DAO.ajouterstationDAO import AjouterstationDAO
# from projet_info.Classe.Utilisateur import Utilisateur

# pip install python-dotenv: A toujours executer avant de commencer


class Ajouterstation:
    def ajouter(self, id_liste, id_station):
        station = AjouterstationDAO().add_id_station(id_liste, id_station)
        print("-----------------------------------")
        print("La station avec l'id '{}' a été ajouté à votre liste dont l'identifiant est '{}'.".format(station[1],station[0]))
        print("-----------------------------------")


if __name__ == "__main__":
    Ajouterstation().ajouter("8", "7978787878")


#La classe Session pour chaque utilisateur qui se connecte sans 
#avoir besoin de demander a chaque fois de faire entrer ses 
# identifiant des listes et toute autre chose