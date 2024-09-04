import sys
import csv
import pandas as pd


# Lecture des lignes du CSV à partir de l'entrée standard
reader = csv.reader(sys.stdin)

# Ignorer l'en-tête du CSV
header = next(reader, None)

# Fonction pour convertir en int ou en float
def safe_convert(value, target_type):
    try:
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        else:
            return value
    except ValueError:
        return 0

# Pour chaque ligne des données csv
for line in reader:

    # Convertir la date en objet datetime
    date_cde = pd.to_datetime(line[7])

    # Ignorer la ligne si année 2004
    if date_cde.year == 2004:
        continue

    # Ignorer la ligne si nombre de colonnes innexact
    if len(line) != 25:
        print(f"Attention : La ligne {line} n'a pas exactement 25 colonnes. Cette ligne sera ignorée.")
        continue
    
    # On ignore les données qui ont une valeur nulle
    for value in line:
        print(value)
        print(type(value))
        if value is None:
            continue

    code_cli = line[0]
    genre_cli = line[1]
    nom_cli = line[2]
    prenom_cli = line[3]
    cp_cli = line[4]
    ville_cli = line[5]
    code_cde = line[6]
    #date_cde = line[7]
    timbre_cli = line[8]
    timbre_cde = line[9]
    nb_colis = safe_convert(line[10], int)
    cheque_cli = line[11]
    barchive = line[12]
    bstock = line[13]
    code_obj = line[14] 
    qte = safe_convert(line[15], int)
    colis = line[16]
    lib_obj = line[17]
    taille_obj = line[18]
    poids_obj = safe_convert(line[19], float)
    points = safe_convert(line[20], int)
    indisp_obj = line[21]
    lib_condit = line[22]
    prix_cond = safe_convert(line[23], float)
    pu_obj = safe_convert(line[24], float) 

    print('%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%i;%s;%s;%s;%s;%i;%s;%s;%s;%f;%i;%s;%s;%f;%f' % (
        code_cli, genre_cli, nom_cli, prenom_cli, cp_cli, ville_cli, code_cde,
        date_cde, timbre_cli, timbre_cde, nb_colis, cheque_cli, barchive, bstock,
        code_obj, qte,colis, lib_obj, taille_obj, poids_obj, points, indisp_obj,
        lib_condit, prix_cond, pu_obj
        ))

# Commande à entrer dans terminal linux pour tester
# cat dataw_fro03_mini_1000.csv | python3 mapper.py