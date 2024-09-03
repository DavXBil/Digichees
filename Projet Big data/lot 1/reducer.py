#!/usr/bin/env python3
import sys
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

listClient = []

# Lecture de chaque ligne d'entrée
for line in sys.stdin:
    # Suppression des espaces blancs
    line = line.strip()
    # Décomposition de la ligne
    parts = line.split(';')


    codcli = parts[0]
    nomcli = parts[1]
    prenomcli = parts[2]
    villecli = parts[3]
    codedep = parts[4]
    libobj = parts[5]
    qte = int(parts[6])
    pointsFidelite = int(parts[7])

    
    client = {
        'codeClient' : codcli,
        'nomClient' : nomcli,
        'prenomClient' : prenomcli,
        'villeClient' : villecli,
        'codeDepartement' : codedep,
        'nomProduit' : libobj,
        'pointsFidelite' : pointsFidelite,
        'quantiteCommande' : qte
    }
    listClient.append(client)

listDeCommandes = pd.DataFrame(listClient)

#client_sum_quantite = listDeCommandes.groupby('codeClient','nomProduit')['quantiteCommande'].sum()

client_sum_pointsFidelite= listDeCommandes.groupby('codeClient')['pointsFidelite'].sum()

top10 = client_sum_pointsFidelite.nlargest(10, 'pointsFidelite')

top10_info = top10.merge(listDeCommandes[['codeClient', 'nomClient', 'prenomClient', 'villeClient', 'codeDepartement' , 'nomProduit' ,'quantiteCommande']], on='codeClient').drop_duplicates()

# Exporter les données agrégées dans un fichier Excel
with pd.ExcelWriter('listDeCommandes_aggregated.xlsx', engine='xlsxwriter') as writer:
    top10_info.to_excel(writer, sheet_name='Top10listDeCommandes', index=False)

    # # Ajouter une feuille pour chaque client
    # for client_code in top10_info['codeClient']:
    #     client_data = listDeCommandes[listDeCommandes['codeClient'] == client_code]

    #     # Exporter les données par client
    #     client_data.to_excel(writer, sheet_name=f'Client_{client_code}', index=False)

# Créer des graphiques en secteurs pour chaque client et les sauvegarder en PDF
for client_code in top10_info['codeClient']:
    client_data = listDeCommandes[listDeCommandes['codeClient'] == client_code]

    # Création du graphique
    plt.figure(figsize=(10, 7))
    plt.pie(client_data['quantiteCommande'], labels=client_data['nomProduit'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Repartition des produits commandés - Client {client_code}')
    
    # Sauvegarder le graphique en PDF
    plt.savefig(f'client_{client_code}_repartition.pdf')
    plt.close()
