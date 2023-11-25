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


app = FastAPI()


class Liste(BaseModel):
    id_liste: int
    nom_liste: str


@app.get("/distincts/elements/carburants&services/")
async def get_distinct_information():
    station = StationsService()
    return station.get_distinct_elements()


@app.get(
    "/recherche/par/filtres/adresse/{n}/{services_recherches}/{carburant_recherche}/{adresse_utilisateur}"
)
async def obtenir_informations_station_par_adresse(
    n: int, services_recherches: str, carburant_recherche: str, adresse_utilisateur: str
):
    stations_service = StationsService()
    response_data = stations_service.trouver_stations_par_filtres_adresse(
        n, services_recherches, carburant_recherche, adresse_utilisateur
    )
    return JSONResponse(content=response_data)


@app.get(
    "/recherche/par/filtres/{n}/{services_recherches}/{carburant_recherche}/{latitude}/{longitude}"
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


# List all favorite lists
@app.get("/listesFav/{id_utilisateur}}", response_model=PyList[Liste])
async def get_listes_favorites():
    user_id = id_utilisateur
    consulter = ConsulterListesFavoris()
    listes = consulter.consulter_listes(user_id)
    if not listes:
        raise HTTPException(status_code=404, detail="Aucune liste de favoris trouvée.")
    return listes


""" @app.get("/stations/informations/{id_station}")
async def obtenir_informations_station(id_station: int):
    stations_service = StationsService()
    return stations_service.trouver_informations_par_id(id_station) """


@app.post("/creer_liste", response_model=Liste)
async def creer_liste(nom_liste: str, id_utilisateur: int):
    consulter = ConsulterListesFavoris()
    nouvelle_liste_creee = consulter.creer_nouvelle_liste(
        id_utilisateur=id_utilisateur, nom_liste=nom_liste
    )
    return nouvelle_liste_creee


@app.delete("/retirer_liste", response_model=bool)
async def retirer_liste(id_utilisateur: int, id_liste: int):
    consulter = ConsulterListesFavoris()
    liste_retiree = consulter.retirer_liste(
        id_utilisateur=id_utilisateur, id_liste=id_liste
    )
    return liste_retiree


# ajouter une station dans une liste
@app.post("/ajouter_station/{id_liste}/{id_station}")
async def ajouter_station(id_liste, id_station):
    station_modifier = ModifStationListes()
    try:
        response = station_modifier.ajouter_station(id_liste, id_station)
        return response
    except Exception as e:
        print(f"Erreur : {e}")
        raise HTTPException(status_code=500, detail="Erreur interne du serveur.")


@app.delete("/retirer_station/{id_liste}/{id_station}", response_model=Dict)
async def retirer_station(id_liste: int, id_station: str):
    station_modifier = ModifStationListes()
    try:
        response = station_modifier.remove_station(id_liste, id_station)
        return response
    except Exception as e:
        print(f"Erreur : {e}")
        raise HTTPException(status_code=500, detail="Erreur interne du serveur.")


@app.get("/get/information/liste/{id_liste}")
async def get_information_liste(id_liste: int):
    favoris = ConsulterListesFavoris()
    return favoris.information_liste(id_liste)


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=80)
