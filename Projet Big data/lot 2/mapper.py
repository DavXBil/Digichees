import sys
import csv
import pandas as pd 

# Lecture des lignes du CSV à partir de l'entrée standard
reader = csv.reader(sys.stdin)

# Ignorer l'en-tête du CSV
header = next(reader, None)


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

def null_convert(value, target_type):
    try:
        if target_type == int:
            return int(value)
    except ValueError:
        return None


def get_year(value):
    try:
        return pd.to_datetime(value).year
    except ValueError:
        return None

def get_departement(value):
    try:
        return int(value[:2])
    except ValueError:
        return None

listeDepartement = [22,49,53]

for line in reader:

    if len(line) != 25:

        print(f"Attention : La ligne {line} n'a pas exactement 25 colonnes. Cette ligne sera ignorée !!!!")
        continue  # Ignorer la ligne

    #codcli = line[0]
    #genrecli = line[1]
    #nomcli = line[2]
    #prenomcli = line[3]
    cpcli = line[4]
    codedep = get_departement(cpcli)
    villecli = line[5]
    codcde = line[6]
    datcde = line[7]
    anneecde = get_year(datcde)
    timbrecli = null_convert(line[8], float)
    timbrecde = safe_convert(line[9], float)
    #Nbcolis = safe_convert(line[10], int)
    #cheqcli = line[11]
    #barchive = line[12]
    #bstock = line[13]
    #codobj = line[14] 

    # Si qte est null dans les données recues on met 0, sinon , on garde sa valeur
    qte = 0 if line[15] == None else safe_convert(line[15], int)

    #Colis = line[16]
    #libobj = line[17]
    #Tailleobj = line[18]
    Poidsobj = safe_convert(line[19], float)

    # Si points est null dans les données recues on met 0, sinon , on garde sa valeur
    #points = 0 if line[20] == None else safe_convert(line[20], int)

    #indispobj = line[21]
    #libcondit = line[22]
    #prixcond = safe_convert(line[23], float)
    #puobj = safe_convert(line[24], float) 

    # Si l'annee de commande est entre 2008 et 2021 on continue , sinon next 
    if (anneecde != None and anneecde >= 20011 and anneecde <= 2016):

    # Si le code de departement est dans la liste listeDepartement 
        if (codedep != None and codedep in listeDepartement ):
        
            if(timbrecli == None or timbrecli == 0):

                # formatage s = string et i = int
                print('%s;%s;%i;%f;%f;%f;%i' % (
                        codcde,villecli,qte,timbrecli if timbrecli is not None else 0,timbrecde,Poidsobj,codedep
                    ))

## cat dataw_fro03.csv | python3 LOT_2/mapper.py 
## cat dataw_fro03.csv | python3 LOT_2/mapper.py | sort | python3 LOT_2/reducer.py
