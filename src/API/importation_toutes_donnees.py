import requests
import zipfile
import io
import xml.etree.ElementTree as ET
from Classe.Coordonnees import Coordonnees
from Classe.TypeCarburant import TypeCarburant
from Classe.Service import Services
from helper import *
import datetime

# from flask import jsonify
import json

# il faut que j'utilise les classes dans le premier code pour avoir directement les stations à la fin
# découper en 2 méthodes je pense, c'est long là
# faire deux fonctions pour récupérer les différents services et carburant


def get_distinct_elements():
    """
    Récupère et retourne tous les éléments distincts du fichier XML compressé, convertis en instances de classe.

    Args:
        url (str): L'URL du fichier XML compressé.

    Returns:
        list: Liste d'instances de la classe Carburant.
        list: Liste d'instances de la classe Services.
    """
    url = "https://donnees.roulez-eco.fr/opendata/instantane"
    carburants_temp = set()
    services_temp = set()

    try:
        response = requests.get(url)

        if response.status_code == 200:
            zip_content = response.content

            with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
                xml_file_name = "PrixCarburants_instantane.xml"

                if xml_file_name in zip_file.namelist():
                    xml_content = zip_file.read(xml_file_name).decode("latin-1")
                    root = ET.fromstring(xml_content)

                    for pdv_element in root.findall(".//pdv"):
                        for carburant_element in pdv_element.findall(".//prix"):
                            carburants_temp.add(
                                (
                                    carburant_element.get("id"),
                                    carburant_element.get("nom"),
                                )
                            )

                        for service_element in pdv_element.findall(
                            ".//services/service"
                        ):
                            services_temp.add(service_element.text)

                else:
                    print(
                        f"Le fichier {xml_file_name} n'est pas présent dans le fichier ZIP."
                    )

        else:
            print(
                f"La requête a échoué avec le code de statut : {response.status_code}"
            )

    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête : {e}")
    except ET.ParseError:
        print("Le contenu extrait n'est pas un fichier XML valide.")

    # Convertir les éléments temporaires en instances de classe
    carburants = [
        TypeCarburant(carburant_id, carburant_nom)
        for carburant_id, carburant_nom in carburants_temp
    ]
    services = [Services(nom) for nom in services_temp]

    return carburants, services


# Exemple d'utilisation

carburants, services = get_distinct_elements()

# Affichage des carburants et services
print("Carburants distincts:")
for carburant in carburants:
    print(carburant)

print("\nServices distincts:")
for service in services:
    print(service)


def trouver_stations_par_filtres(
    n: int,
    services_recherches: list,
    carburants_recherches: list,
    coor_utilisateur: Coordonnees,
):
    # pour les services, mettre liste vide si aucun filtre dessus
    # pour les carburants, tous les mettre ["Gazole", "E10", "GPLc","SP98","SP95","E85"]
    # on pourra rajouter aussi le paramètre horaire après

    url = "https://donnees.roulez-eco.fr/opendata/instantane"

    debut_execution = datetime.datetime.now()
    print(f"Début d'exécution : {debut_execution}")

    try:
        response = requests.get(url)

        if response.status_code == 200:
            zip_content = response.content

            with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
                xml_file_name = "PrixCarburants_instantane.xml"

                if xml_file_name in zip_file.namelist():
                    xml_content = zip_file.read(xml_file_name).decode("latin-1")
                    root = ET.fromstring(xml_content)

                    # Créez une liste pour stocker les informations
                    ids = []
                    latitude = []
                    longitude = []
                    cp = []
                    adresse = []

                    # Parcourez tous les éléments <pdv> dans le XML
                    for pdv_element in root.findall(".//pdv"):
                        # Obtenez la liste des services pour la station
                        services = [
                            service.text
                            for service in pdv_element.findall(".//services/service")
                        ]
                        carburants = [
                            carburant_element.get("nom")
                            for carburant_element in pdv_element.findall(".//prix")
                        ]

                        # Vérifiez si les services recherchés sont présents dans la liste des services
                        if all(service in services for service in services_recherches):
                            if any(
                                carburant in carburants_recherches
                                for carburant in carburants
                            ):
                                # on récupère les informations relatives à l'id et la localisation
                                # de la station
                                pdv_id = pdv_element.get("id")
                                pdv_latitude = pdv_element.get("latitude")
                                pdv_longitude = pdv_element.get("longitude")
                                pdv_cp = pdv_element.get("cp")
                                pdv_adresse = pdv_element.get("adresse")
                                ids.append(pdv_id)
                                latitude.append(pdv_latitude)
                                longitude.append(pdv_longitude)
                                cp.append(pdv_cp)
                                adresse.append(pdv_adresse)

                    coor_info = [
                        Coordonnees(
                            pdv_id,
                            float(pdv_latitude) / 100000,
                            float(pdv_longitude) / 100000,
                            pdv_adresse,
                        )
                        for pdv_id, pdv_latitude, pdv_longitude, pdv_adresse in zip(
                            ids, latitude, longitude, adresse
                        )
                    ]

                    dist = []
                    for x in coor_info:
                        y = x.dist(coor_utilisateur)
                        dist.append(y)
                    # print(dist)

                    print(len(coor_info))

                    dist_triee = trier(dist)

                    # print(dist_triee)

                    dist_triee_premiers = selectionner_n_premiers(n, dist_triee)
                    print(dist_triee_premiers)

        else:
            print("La requête a échoué avec le code de statut :", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Erreur de requête :", e)
    except ET.ParseError:
        print("Le contenu extrait n'est pas un fichier XML valide.")


trouver_stations_par_filtres(
    5, [], ["Gazole"], Coordonnees(0, 48.6428477, 2.7143162, "3 rue")
)


def trouver_informations_par_id(id_station: int):
    url = "https://donnees.roulez-eco.fr/opendata/instantane"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            zip_content = response.content

            with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
                xml_file_name = "PrixCarburants_instantane.xml"

                if xml_file_name in zip_file.namelist():
                    xml_content = zip_file.read(xml_file_name).decode("latin-1")
                    root = ET.fromstring(xml_content)

                    # Recherche de la station par son identifiant
                    pdv_element = root.find(".//pdv[@id='{}']".format(id_station))

                    if pdv_element is not None:
                        # Récupérez les informations de la station directement comme un dictionnaire
                        station_info = {
                            "id": pdv_element.get("id"),
                            "latitude": float(pdv_element.get("latitude")) / 100000,
                            "longitude": float(pdv_element.get("longitude")) / 100000,
                            "cp": pdv_element.get("cp"),
                            "adresse": pdv_element.findtext(".//adresse"),
                        }
                        return station_info
                    else:
                        return None
                else:
                    return {
                        "error": "Le fichier XML attendu n'est pas présent dans l'archive."
                    }

        else:
            return {
                "error": "La requête a échoué avec le code de statut {}".format(
                    response.status_code
                )
            }

    except requests.exceptions.RequestException as e:
        # Loggez l'erreur
        print(f"Erreur de requête : {e}")
        return {"error": "Erreur de requête : {}".format(e)}

    except ET.ParseError:
        return {"error": "Le contenu extrait n'est pas un fichier XML valide."}


def info_stations_preferees(liste: list):
    resultats = []

    for id_station in liste:
        informations_station = trouver_informations_par_id(id_station)

        if informations_station:
            resultats.append(informations_station)

    # Utilisez jsonify pour convertir la liste de dictionnaires en JSON
    return json.dumps(resultats, indent=2)


id_station_recherche = 74800004
resultat = trouver_informations_par_id(id_station_recherche)
if resultat:
    print(resultat)
else:
    print("Aucune station trouvée avec l'identifiant", id_station_recherche)

liste_station = [74800004, 77390005, 77390003]
print(info_stations_preferees(liste_station))
