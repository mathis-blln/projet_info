from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from DAO.listeDAO import ListeDAO


app = FastAPI()


class Liste(BaseModel):
    id_liste: str
    nom: str


# Create a dictionary to store characters
listes_db: Dict[int, Liste] = {}


# List all favorite lists
@app.get("/listesFav/")  # c'est ici qu'on spécifie les identifiants
async def get_liste_stations():  # et là
    global listes_db
    Listes = ListeDAO().find_all_listes("8")  # identifiant utilisateur (8)
    for i in range(len(Listes)):
        listes_db["Station " + str(i + 1)] = Liste(
            id_liste=Listes[i].id_liste, nom=Listes[i].nom_liste
        )
    return listes_db


# Choose list
@app.get("/listesFav/{numero}")
async def get_station_liste(numero: int):
    global listes_db
    Listes = ListeDAO().find_all_listes("8")
    for i in range(len(Listes)):
        listes_db["Station " + str(i + 1)] = Liste(
            id_liste=Listes[i].id_liste, nom=Listes[i].nom_liste
        )
    return listes_db["Station " + str(numero)]


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=80)
