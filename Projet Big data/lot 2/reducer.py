#!/usr/bin/env python3
import sys
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

listCommande = []

# Lecture de chaque ligne d'entrée
for line in sys.stdin:
    # Suppression des espaces blancs
    line = line.strip()
    # Décomposition de la ligne
    parts = line.split(';')

    codcde = parts[0]
    villecli = parts[1]
    qte = parts[2]
    timbrecli = parts[3]
    timbrecde = float(parts[4])
    poidsobj = float(parts[5])
    codedep = int(parts[6])
    
    commande = {
        'codeCommande' : codcde,
        'villeClient' : villecli,
        'quantiteCommande' : qte,
        'timbreColi' : timbrecli,
        'timbreCommande' : timbrecde,
        'poidsProduit' : poidsobj,
        'departement' : codedep,
    }
    listCommande.append(commande)

dfCmd = pd.DataFrame(listCommande)

cmd_sum_timbre_cmd = dfCmd.groupby('codeCommande')['timbreCommande'].sum()

top100 = pd.DataFrame(cmd_sum_timbre_cmd.nlargest(100))

top100_info = top100.merge(dfCmd[['codeCommande', 'villeClient', 'quantiteCommande', 'timbreColi','poidsProduit' ,'departement']], on='codeCommande').drop_duplicates()

top_5_percent_random = top100_info.sample(frac=0.05)

# Exporter les données agrégées dans un fichier Excel
with pd.ExcelWriter('LOT_2/top5random_aggregated.xlsx', engine='xlsxwriter') as writer:
    top_5_percent_random.to_excel(writer, sheet_name='top5random_aggregated', index=False)


listeDepartement = [22,49,53]

# Créer des graphiques en secteurs pour chaque client et les sauvegarder en PDF

for departement in listeDepartement:

    # Crée un DF qui contien que les ligne avec le de
    comande = top_5_percent_random[top_5_percent_random['departement'] == departement]

    if not comande.empty:
        

        # Création du graphique
        plt.figure(figsize=(10, 7))
        plt.pie(comande['timbreCommande'], labels=comande['villeClient'], autopct='%1.1f%%', startangle=140)
        plt.title(f'Repartition des produits commandés par ville par departement {departement} avec {len(comande)} commandes')
        
        # Sauvegarder le graphique en PDF
        plt.savefig(f'LOT_2/departement_{departement}_repartition.pdf')
        plt.close()
    else:
        print(f'Aucune ligne trouvée où le département est {departement}.')
