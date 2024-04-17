from datetime import date, datetime
print(date(2016, 7, 4).isocalendar())

def nettoyeur_txt(filename):
    # Ouverture du fichier et premier nettoyage des données inutilisables
    with open(filename,'r') as file :
        file_input = file.read().split('\n')
        rows = []
        for row in file_input :
            rows.append(row.split('\t'))
    del rows[0]

    #Récupération des dates
    dico_date = {1 : "Lundi", 2 : "Mardi", 3 : "Mercredi", 4 : "Jeudi", 5 : "Vendredi", 6 : "Samedi", 7 : "Dimanche"}
    new_rows = [['Date','Jour','Semaine','Libelle_ligne','Categorie_titre','Nb_valid']]
    for row in rows :
        if '/' in row[0] :
            annee,numero_semaine,numero_jour = date(int(row[0][6:]),int(row[0][3:5]),int(row[0][0:2])).isocalendar()
            if "Moins de" in row[-1] :
                new_rows.append([row[0],dico_date[numero_jour],numero_semaine,row[4],row[-2],"Moins de 5"])
            else :
                #On nettoie la colonne du nombre de validations :
                compteur = -1
                while row[-1][compteur] != " " :
                    compteur -= 1
                new_rows.append([row[0],dico_date[numero_jour],numero_semaine,row[4],row[-2],row[-1][compteur+1:]])
    return new_rows

data = nettoyeur_txt(r"Data\1e-semestre-2018.txt")

import csv

with open(r'Data\1e-sem-2018.csv','w',newline='') as fp :
    writer = csv.writer(fp)
    writer.writerows(data)