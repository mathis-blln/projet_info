import psycopg2

# Établir une connexion à la base de données
conn = psycopg2.connect(
    host="votre_hote",
    database="votre_base_de_donnees",
    user="votre_utilisateur",
    password="votre_mot_de_passe"
)

# Créer un curseur
cur = conn.cursor()

# Requête SQL pour créer la table
create_table_query = """
CREATE TABLE ma_table (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255),
    age INT
);
"""

# Exécuter la requête pour créer la table
cur.execute(create_table_query)

# Valider la transaction et fermer la connexion
conn.commit()
conn.close()
