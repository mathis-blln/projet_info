from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from DAO.listeDAO import ListeDAO
from typing import List as PyList
from Services.consulterListeFavoris import ConsulterListesFavoris


app = FastAPI()


class Liste(BaseModel):
    id_liste: int
    nom_liste: str
    id_utilisateur: int


# Create a dictionary to store characters
listes_db: Dict[int, Liste] = {}

"""
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
"""


# Crée une instance du service
consulter_listes_service = ConsulterListesFavoris()


# List all favorite lists
@app.get("/listesFav/{id_user}", response_model=PyList[Liste])
async def get_listes_favorites(id_user):
    consulter = ConsulterListesFavoris()
    listes = consulter.consulter_listes2(id_user)
    if not listes:
        raise HTTPException(status_code=404, detail="Aucune liste de favoris trouvée.")
    return listes


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
