from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from DAO.listeDAO import ListeDAO
from typing import List as PyList
from Services.consulterListeFavoris import ConsulterListesFavoris
from Services.service_station import StationsService
from typing import Optional  # Importez Optional
from Services.modif_stations_de_listes import ModifStationListes
import json
from fastapi.responses import JSONResponse
import datetime
from Session import Session


app2 = FastAPI()


@app2.get(
    "/distincts/elements/carburants&services/",
    description="Obtenir tous les services et carburants distincts dans le fichier XML",
)
async def get_distinct_information():
    station = StationsService()
    return station.get_distinct_elements()


@app2.get(
    "/recherche/par/filtres/adresse/{n}/{services_recherches}/{carburant_recherche}/{adresse_utilisateur}",
    description="Obtenir toutes les stations correspondant à un filtre choisi utilisant l'adresse",  # noqa: E501
)
async def obtenir_informations_station_par_adresse(
    n: int, services_recherches: str, carburant_recherche: str, adresse_utilisateur: str
):
    stations_service = StationsService()
    response_data = stations_service.trouver_stations_par_filtres_adresse(
        n, services_recherches, carburant_recherche, adresse_utilisateur
    )
    return JSONResponse(content=response_data)


@app2.get(
    "/recherche/par/filtres/{n}/{services_recherches}/{carburant_recherche}/{latitude}/{longitude}",
    description="Obtenir toutes les stations correspondant à un filtre choisi utilisant les coordonnées latitude et longitude",  # noqa: E501
)
async def obtenir_informations_station(
    n: int,
    services_recherches: str,
    carburant_recherche: str,
    latitude: float,
    longitude: float,
):
    stations_service = StationsService()
    response_data = stations_service.trouver_stations_par_filtres(
        n, services_recherches, carburant_recherche, latitude, longitude
    )
    return JSONResponse(content=response_data)


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app2, host="127.0.0.1", port=8000)
