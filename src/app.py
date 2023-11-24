from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from DAO.listeDAO import ListeDAO
from typing import List as PyList
from Services.consulterListeFavoris import ConsulterListesFavoris
from Services.service_station import StationsService


app = FastAPI()


class Liste(BaseModel):
    id_liste: int
    nom_liste: str
    id_utilisateur: int


# Create a dictionary to store characters
listes_db: Dict[int, Liste] = {}


# List all favorite lists
@app.get("/listesFav/{id_user}", response_model=PyList[Liste])
async def get_listes_favorites(id_user):
    consulter = ConsulterListesFavoris()
    listes = consulter.consulter_listes(id_user)
    if not listes:
        raise HTTPException(status_code=404, detail="Aucune liste de favoris trouvée.")
    return listes


@app.get("/distincts/elements/carburants&services/")
async def get_distinct_information():
    station = StationsService()
    return station.get_distinct_elements()


@app.get("/stations/informations/{id_station}")
async def obtenir_informations_station(id_station: int):
    stations_service = StationsService()
    return stations_service.trouver_informations_par_id(id_station)


""" # Choose list
@app.get("/listesFav/{numero}")
async def get_station_liste(numero: int):
    global listes_db
    Listes = ListeDAO().find_all_listes("8")
    for i in range(len(Listes)):
        listes_db["Station " + str(i + 1)] = Liste(
            id_liste=Listes[i].id_liste, nom=Listes[i].nom_liste
        )
    return listes_db["Station " + str(numero)] """


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=80)
