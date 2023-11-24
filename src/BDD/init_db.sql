-- Active: 1699913521992@@sgbd-eleves.domensai.ecole@5432@id2377
DROP SCHEMA IF EXISTS projet CASCADE;
CREATE SCHEMA projet;

--------------------------------------------------------------
-- Les stations
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.stations CASCADE ;
CREATE TABLE projet.stations (
    id_stations text PRIMARY KEY,
    adresse text NOT NULL,
    ville text NOT NULL
);


--------------------------------------------------------------
-- Les services
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.utilisateur CASCADE ;

CREATE TABLE projet.utilisateur (
    id_utilisateur INT PRIMARY KEY,
    nom_utilisateur text NOT NULL,
    mdp text NOT NULL
);

--------------------------------------------------------------
-- Les listes des stations
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.listes CASCADE ;

CREATE TABLE projet.listes (
    id_liste SERIAL PRIMARY KEY,
    id_utilisateur text REFERENCES projet.utilisateur(id_utilisateur),
    nom_liste text UNIQUE NOT NULL
);

--------------------------------------------------------------
-- Le contenu des listes des stations
--------------------------------------------------------------


DROP TABLE IF EXISTS projet.contenu_liste CASCADE ;

CREATE TABLE projet.contenu_liste (
    id_liste SERIAL REFERENCES projet.listes(id_liste),
    id_stations text 
);