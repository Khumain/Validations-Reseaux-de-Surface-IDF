import csv

def nbre_valid_jour(semestre):
    Nombre_validation_semestre = [[0,0,0,0,0,0,0,0,0] for i in range(7)]
    Jours_possibles = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
    Titres_possibles = ['IMAGINE R', 'NON DEFINI', 'AUTRE TITRE', 'FGT', 'NAVIGO', 'AMETHYSTE', 'TST','?','NAVIGO JOUR','AUTRES']
    with open(r'Data//' + semestre) as fichier:
        reader = csv.reader(fichier)
        next(reader)
        rows = []
        for row in reader:
#            if row[1] not in Titres_possibles:
 #               row[4]=row[4].replace(row[4],'AUTRE TITRE')

#                Titres_possibles.append(row[1])
 #               for i in range(7):
  #                  Nombre_validation_semestre[i].append(0)
            if row[5] == 'Moins de 5':
                row[5]=row[5].replace('Moins de 5','0')
            elif row[1] == 'lundi' or row[1] == 'Lundi':
                i=0
                while row[4]!=Titres_possibles[i]:
                    i+=1
                Nombre_validation_semestre[0][i]+=int(row[5])
            elif row[1] == 'mardi' or row[1] == 'Mardi':
                i=0
                while row[4]!=Titres_possibles[i]:
                    i+=1
                Nombre_validation_semestre[1][i]+=int(row[5])
            elif row[1] == 'mercredi' or row[1] == 'Mercredi':
                i=0
                while row[4]!=Titres_possibles[i]:
                    i+=1
                Nombre_validation_semestre[2][i]+=int(row[5])
            elif row[1] == 'jeudi' or row[1] == 'Jeudi':
                i=0
                while row[4]!=Titres_possibles[i]:
                    i+=1
                Nombre_validation_semestre[3][i]+=int(row[5])
            elif row[1] == 'vendredi' or row[1] == 'Vendredi':
                i=0
                while row[4]!=Titres_possibles[i]:
                    i+=1
                Nombre_validation_semestre[4][i]+=int(row[5])
            elif row[1] == 'samedi' or row[1] == 'Samedi':
                i=0
                while row[4]!=Titres_possibles[i]:
                    i+=1
                Nombre_validation_semestre[5][i]+=int(row[5])
            else : #row[1] == 'dimanche' or row[1] == 'Dimanche':
                i=0
                while row[4]!=Titres_possibles[i]:
                    i+=1
                Nombre_validation_semestre[6][i]+=int(row[5])
    return(Nombre_validation_semestre)

#print(nbre_valid_jour("1e-sem-2016.csv"))

def tran(semestre):
    h=[]
    res={}
    liste=nbre_valid_jour(semestre)
    for l in liste :
        d={}
        d['IMAGINE R']=l[0]
        d['NON DEFINI']=l[1]
        d['AUTRE TITRE']=l[2]
        d['FGT']=l[3]
        d['NAVIGO']=l[4]
        d['AMETHYSTE']=l[5]
        d['TST']=l[6]
        d['?']=l[7]
        d['NAVIGO JOUR']=l[8]
        h.append(d)
    res['Lundi']=h[0]
    res['Mardi']=h[1]
    res['Mercredi']=h[2]
    res['Jeudi']=h[3]
    res['Vendredi']=h[4]
    res['Samedi']=h[5]
    res['Dimanche']=h[6]
    return(res)

