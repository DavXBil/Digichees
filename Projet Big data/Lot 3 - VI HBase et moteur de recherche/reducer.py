import sys
import happybase

# Connexion
connection = happybase.Connection('127.0.0.1', 9090)
connection.open()
table = connection.table('digicheese_data')

# Dictionnaire pour stocker les données
all_data = {}

# Lecture des données en provenance du mapper
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # Split des données sur le point-virgule
    parts = line.split(';') 

    # Affichage des résultats et insertion dans HBase


# Fermer la connexion à HBase
connection.close()
