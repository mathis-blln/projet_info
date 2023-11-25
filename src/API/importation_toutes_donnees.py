import requests
import zipfile
import io
import xml.etree.ElementTree as ET
from Classe.Coordonnees import Coordonnees
from Classe.TypeCarburant import TypeCarburant
from Classe.Service import Services
from helper import *
from geopy.geocoders import Nominatim
import datetime
from Classe.Station import Station
from Classe.PrixCarburant import PrixCarburant

# from flask import jsonify
import json


# il faut que j'utilise les classes dans le premier code pour avoir directement les stations à la fin
# il faut que je transforme en vrai objet station (donc redéfinir les classes)
def trouver_stations_par_filtres_adresse(
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
                            for service in pdv_element.findall(".//services/service")
                        ]
                        carburants = [
                            carburant_element.get("nom")
                            for carburant_element in pdv_element.findall(".//prix")
                        ]

                        if all(service in services for service in services_recherches):
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
                                for carburant_element in pdv_element.findall(".//prix")
                                if carburant_element.get("nom") == carburants_recherches
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
                    dist_triee_premiers = extraire_premier_element(dist_triee_premiers)

                    response_json = {
                        "requete": {
                            "services_recherches": services_recherches,
                            "carburants_recherches": carburants_recherches,
                            "adresse": adresse_utilisateur,
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

                    return json.dumps(response_json, indent=4)

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


print(
    trouver_stations_par_filtres_adresse(
        5, "Lavage automatique", "Gazole", "la renouette, laillé"
    )
)
