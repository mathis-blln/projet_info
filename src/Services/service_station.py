import requests
import zipfile
import io
import xml.etree.ElementTree as ET
from Classe.Coordonnees import Coordonnees
from Classe.TypeCarburant import TypeCarburant
from Classe.Service import Services
from Classe.Station import Station
from Classe.PrixCarburant import PrixCarburant
from helper import *
from geopy.geocoders import Nominatim
import datetime

# from flask import jsonify
import json

# il faut que j'utilise les classes dans le premier code pour avoir directement les stations à la fin
# il faut que je transforme en vrai objet station (donc redéfinir les classes)


class StationsService:
    def get_distinct_elements(self):
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

    def trouver_stations_par_filtres(
        self,
        n: int,
        services_recherches: str,
        carburants_recherches: str,
        latitude: float,
        longitude: float,
    ):
        coor_utilisateur = Coordonnees(0, latitude, longitude, "adresse")

        url = "https://donnees.roulez-eco.fr/opendata/instantane"

        services_recherches = split_input(services_recherches)

        try:
            response = requests.get(url)

            if response.status_code == 200:
                zip_content = response.content

                with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
                    xml_file_name = "PrixCarburants_instantane.xml"

                    if xml_file_name in zip_file.namelist():
                        xml_content = zip_file.read(xml_file_name).decode("latin-1")
                        root = ET.fromstring(xml_content)

                        ids = []
                        latitude = []
                        longitude = []
                        cp = []
                        ville = []
                        adresse = []
                        carburants_list = []

                        for pdv_element in root.findall(".//pdv"):
                            services = [
                                service.text
                                for service in pdv_element.findall(
                                    ".//services/service"
                                )
                            ]
                            carburants = [
                                carburant_element.get("nom")
                                for carburant_element in pdv_element.findall(".//prix")
                            ]

                            if all(
                                service in services for service in services_recherches
                            ):
                                if any(
                                    carburant in carburants_recherches
                                    for carburant in carburants
                                ):
                                    pdv_id = pdv_element.get("id")
                                    pdv_latitude = pdv_element.get("latitude")
                                    pdv_longitude = pdv_element.get("longitude")
                                    pdv_cp = pdv_element.get("cp")
                                    pdv_ville = pdv_element.get("ville")
                                    pdv_adresse = pdv_element.findtext(".//adresse")
                                    ids.append(pdv_id)
                                    latitude.append(pdv_latitude)
                                    longitude.append(pdv_longitude)
                                    cp.append(pdv_cp)
                                    ville.append(pdv_ville)
                                    adresse.append(pdv_adresse)

                                    carburants_list.append(carburants)

                        stations = [
                            Station(
                                pdv_id,
                                pdv_cp,
                                pdv_ville,
                                pdv_adresse,
                                Coordonnees(
                                    pdv_id,
                                    float(pdv_latitude) / 100000,
                                    float(pdv_longitude) / 100000,
                                    pdv_adresse,
                                ),
                                [
                                    PrixCarburant(
                                        carburant_element.get("id"),
                                        pdv_id,
                                        float(carburant_element.get("valeur")),
                                    )
                                    for carburant_element in pdv_element.findall(
                                        ".//prix"
                                    )
                                    if carburant_element.get("nom")
                                    == carburants_recherches
                                ],
                            )
                            for pdv_id, pdv_cp, pdv_ville, pdv_adresse, pdv_latitude, pdv_longitude, carburants in zip(
                                ids,
                                cp,
                                ville,
                                adresse,
                                latitude,
                                longitude,
                                carburants_list,
                            )
                        ]

                        dist = []
                        for x in stations:
                            y = x.coordonnees.dist(coor_utilisateur)
                            dist.append(y)

                        longueur = len(stations)

                        dist_triee = trier(dist)
                        dist_triee_premiers = selectionner_n_premiers(n, dist_triee)
                        dist_triee_premiers = extraire_premier_element(
                            dist_triee_premiers
                        )

                        response_json = {
                            "Voici les éléments de votre requête": {
                                "services recherches": services_recherches,
                                "carburants recherches": carburants_recherches,
                                "coordonnees": {
                                    "latitude entrée ": coor_utilisateur.latitude,
                                    "longitude entrée": coor_utilisateur.longitude,
                                },
                            },
                            "date_heure_execution": str(datetime.datetime.now()),
                            "nombre_stations_trouvees": longueur,
                            "liste_stations": [
                                {
                                    "id": station.id_station,
                                    "coordonnees": {
                                        "latitude": station.coordonnees.latitude,
                                        "longitude": station.coordonnees.longitude,
                                    },
                                    "adresse": station.adresse,
                                    "cp": station.cp,
                                    "prix_carburant": [
                                        {
                                            "prix": prix_carburant.prix,
                                        }
                                        for prix_carburant in station.prix_carburant
                                    ],
                                }
                                for station in stations
                                if station.id_station in dist_triee_premiers
                            ],
                        }

                        return json.dumps(response_json, indent=4, ensure_ascii=False)

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

    def trouver_stations_par_filtres_adresse(
        self,
        n: int,
        services_recherches: str,
        carburants_recherches: str,
        adresse_utilisateur: str,
    ):
        coor = adresse_en_coordonnees(adresse_utilisateur)

        if coor:
            coor_utilisateur = Coordonnees(0, coor[0], coor[1], "adresse")
        else:
            print("La transformation d'adresse en coordonnées a échoué.")
            return

        url = "https://donnees.roulez-eco.fr/opendata/instantane"

        services_recherches = split_input(services_recherches)

        try:
            response = requests.get(url)

            if response.status_code == 200:
                zip_content = response.content

                with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
                    xml_file_name = "PrixCarburants_instantane.xml"

                    if xml_file_name in zip_file.namelist():
                        xml_content = zip_file.read(xml_file_name).decode("latin-1")
                        root = ET.fromstring(xml_content)

                        ids = []
                        latitude = []
                        longitude = []
                        cp = []
                        ville = []
                        adresse = []
                        carburants_list = []

                        for pdv_element in root.findall(".//pdv"):
                            services = [
                                service.text
                                for service in pdv_element.findall(
                                    ".//services/service"
                                )
                            ]
                            carburants = [
                                carburant_element.get("nom")
                                for carburant_element in pdv_element.findall(".//prix")
                            ]

                            if all(
                                service in services for service in services_recherches
                            ):
                                if any(
                                    carburant in carburants_recherches
                                    for carburant in carburants
                                ):
                                    pdv_id = pdv_element.get("id")
                                    pdv_latitude = pdv_element.get("latitude")
                                    pdv_longitude = pdv_element.get("longitude")
                                    pdv_cp = pdv_element.get("cp")
                                    pdv_ville = pdv_element.get("ville")
                                    pdv_adresse = pdv_element.findtext(".//adresse")
                                    ids.append(pdv_id)
                                    latitude.append(pdv_latitude)
                                    longitude.append(pdv_longitude)
                                    cp.append(pdv_cp)
                                    ville.append(pdv_ville)
                                    adresse.append(pdv_adresse)

                                    carburants_list.append(carburants)

                        stations = [
                            Station(
                                pdv_id,
                                pdv_cp,
                                pdv_ville,
                                pdv_adresse,
                                Coordonnees(
                                    pdv_id,
                                    float(pdv_latitude) / 100000,
                                    float(pdv_longitude) / 100000,
                                    pdv_adresse,
                                ),
                                [
                                    PrixCarburant(
                                        carburant_element.get("id"),
                                        pdv_id,
                                        float(carburant_element.get("valeur")),
                                    )
                                    for carburant_element in pdv_element.findall(
                                        ".//prix"
                                    )
                                    if carburant_element.get("nom")
                                    == carburants_recherches
                                ],
                            )
                            for pdv_id, pdv_cp, pdv_ville, pdv_adresse, pdv_latitude, pdv_longitude, carburants in zip(
                                ids,
                                cp,
                                ville,
                                adresse,
                                latitude,
                                longitude,
                                carburants_list,
                            )
                        ]

                        dist = []
                        for x in stations:
                            y = x.coordonnees.dist(coor_utilisateur)
                            dist.append(y)

                        longueur = len(stations)

                        dist_triee = trier(dist)
                        dist_triee_premiers = selectionner_n_premiers(n, dist_triee)
                        dist_triee_premiers = extraire_premier_element(
                            dist_triee_premiers
                        )

                        response_json = {
                            "Voici les éléments de votre requête": {
                                "services recherches": services_recherches,
                                "carburants recherches": carburants_recherches,
                                "adresse entrée": adresse_utilisateur,
                            },
                            "date_heure_execution": str(datetime.datetime.now()),
                            "nombre_stations_trouvees": longueur,
                            "liste_stations": [
                                {
                                    "id": station.id_station,
                                    "coordonnees": {
                                        "latitude": station.coordonnees.latitude,
                                        "longitude": station.coordonnees.longitude,
                                    },
                                    "adresse": station.adresse,
                                    "cp": station.cp,
                                    "prix_carburant": [
                                        {
                                            "prix": prix_carburant.prix,
                                        }
                                        for prix_carburant in station.prix_carburant
                                    ],
                                }
                                for station in stations
                                if station.id_station in dist_triee_premiers
                            ],
                        }

                        return json.dumps(response_json, indent=4, ensure_ascii=False)

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

    def trouver_informations_par_id(self, id_station: int):
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
                                "longitude": float(pdv_element.get("longitude"))
                                / 100000,
                                "cp": pdv_element.get("cp"),
                                "adresse": pdv_element.findtext(".//adresse"),
                                "carburants": [],
                            }
                            prix_elements = pdv_element.findall(".//prix")
                            for prix_element in prix_elements:
                                carburant_info = {
                                    "nom": prix_element.get("nom"),
                                    "id": prix_element.get("id"),
                                    "valeur": float(prix_element.get("valeur")),
                                }
                                station_info["carburants"].append(carburant_info)

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

    def info_stations_preferees(self, liste: list):
        debut_execution = datetime.datetime.now()
        print(f"Début d'exécution : {debut_execution}")
        resultats = []

        for id_station in liste:
            informations_station = self.trouver_informations_par_id(id_station)

            if informations_station:
                resultats.append(informations_station)

        return resultats


if __name__ == "__main__":
    station = StationsService()
    print(
        station.trouver_stations_par_filtres(
            5, "Lavage automatique", "Gazole", 42.5, 1.89
        )
    )
