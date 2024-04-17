import datetime
import csv
chemins=[r'Data\1e-semestre-2019.csv',r'Data\2e-semestre-2018.csv']
donnees_utiles=[]
with open(chemins[1],'r',encoding='utf_8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=";")
    next(spamreader)
    n=0
    donnees_utiles.append(['Jour','numero_jour','numero_semaine','LIBELLE_LIGNE', 'CATEGORIE_TITRE', 'NB_VALD'])

    for ligne in spamreader:
        year=int(ligne[0][:4])
        month=int(ligne[0][5:7])
        day=int(ligne[0][8:])
        dt=datetime.date(year,month,day)
        num_jour=dt.isocalendar()[2]
        num_semaine=dt.isocalendar()[1]
        if num_jour==1:
            jour='lundi'
        elif num_jour==2:
            jour='mardi'
        elif num_jour==3:
            jour='mercredi'
        elif num_jour==4:
            jour='jeudi'
        elif num_jour==5:
            jour='vendredi'
        elif num_jour==6:
            jour='samedi'
        elif num_jour==7:
            jour='dimanche'
        donnees_utiles.append([ligne[0],jour,str(num_semaine),ligne[4],ligne[6],ligne[7]])


with open(r'Data\2_sem_2018_utils.csv','w',encoding='utf_8') as fichier:
    for ligne in donnees_utiles:
        fichier.write(",".join(ligne) + "\n")






