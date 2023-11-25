from InquirerPy import prompt
from view.connexion_view import ConnexionView
from view.inscription_view import InscriptionView
from view.menu_view import MenuView  # Importez votre MenuView appropriée

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
import subprocess


def lancer_api():
    # Lancer l'API FastAPI avec uvicorn
    subprocess.Popen(["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "80"])


lancer_api()


class StartView:
    def __init__(self):
        # Initialisez les vues nécessaires ici
        self.connexion_view = ConnexionView()
        self.inscription_view = InscriptionView()
        self.menu_view = MenuView()

    def make_choice(self):
        while True:
            response = prompt(
                {
                    "type": "list",
                    "name": "choix",
                    "message": f"Bonjour",
                    "choices": [
                        "Connexion",
                        "Inscription",
                        "Faire une recherche",
                        "Quitter",
                    ],
                }
            )

            if response["choix"] == "Quitter":
                break

            elif response["choix"] == "Connexion":
                auth_result = self.connexion_view.make_choice()

                if auth_result is None:  # Si l'authentification réussit
                    self.menu_view.display_info()
                    self.menu_view.make_choice()

                if auth_result == "EchecConnexion":
                    continue  # Redémarrer la boucle pour afficher à nouveau les options après l'échec d'authentification

            elif response["choix"] == "Inscription":
                insc_result = self.inscription_view.make_choice()

                if (
                    insc_result == "Connexion"
                ):  # Si l'inscription réussie, rediriger vers la vue Connexion
                    auth_result = self.connexion_view.make_choice()

                    if (
                        auth_result is None
                    ):  # Si l'authentification réussit après l'inscription
                        self.menu_view.display_info()
                        self.menu_view.make_choice()
            return None
