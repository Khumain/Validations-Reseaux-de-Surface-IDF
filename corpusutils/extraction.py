#Ce module sert à créer des fonctions qui permettent d'extraire des stats à partir de la base données Data
#il suffit de taper dans la ligne de commande help(fonction) pour savoir ce que fait chaque fonction
import csv
import numpy as np
titres=['IMAGINE R', 'NON DEFINI', 'AUTRE TITRE', 'FGT', 'NAVIGO', 'AMETHYSTE', 'TST','?','NAVIGO JOUR']
#comment j'ai crée titres
#with open(r'C:/Users/Zakaria/Desktop/data_vis/validations-sur-les-reseaux-de-surface/Data/2e-sem-2018.csv','r') as csvfile:
#                spamreader = csv.reader(csvfile, delimiter=",")
#                next(spamreader)
#                for ligne in spamreader:
#                    titres.append(ligne[-2])
#titres=list(set(titres))
def nombre_de_validation_semestre(semestre):
    '''fonction qui reçoit comme argument un semestre et renvoie un dictionnaire qui contient le nombre de validation par titre'''
    with open(r'Data/'+semestre,'r') as csvfile:#adapter ton chemin jusqu'à arriver à Data
                csvreader = csv.reader(csvfile, delimiter=",")
                next(csvreader)
                n_imag,n_nondef,n_autre,n_fgt,n_navigo,n_ame,n_tst,truc,n_nav_jour=0,0,0,0,0,0,0,0,0
                for ligne in csvreader:
                    if ligne[-2]=='IMAGINE R':
                        n_imag += 1
                    elif ligne[-2]=='NON DEFINI':
                        n_nondef += 1
                    elif ligne[-2]=='AUTRE TITRE':
                        n_autre += 1
                    elif ligne[-2]=='FGT':
                        n_fgt += 1
                    elif ligne[-2]=='NAVIGO':
                        n_navigo += 1
                    elif ligne[-2]=='AMETHYSTE':
                        n_ame += 1
                    elif ligne[-2]=='TST':
                        n_tst += 1
                    elif ligne[-2] == '?':
                        truc += 1
                    elif ligne[-2] == 'NAVIGO JOUR' :
                        n_nav_jour += 1
    dicti ={'IMAGINE R': n_imag, 'NON DEFINI' : n_nondef, 'AUTRE TITRE':n_autre, 'FGT':n_fgt, 'NAVIGO':n_navigo, 'AMETHYSTE': n_ame, 'TST':n_tst,'?':truc,'NAVIGO JOUR':n_nav_jour}
    return(dicti)

    #labels='IMAGINE R', 'NON DEFINI', 'AUTRE TITRE', 'FGT', 'NAVIGO', 'AMETHYSTE', 'TST','?','NAVIGO JOUR'
    #sizes =[n_imag,n_nondef,n_autre,n_fgt,n_navigo,n_ame,n_tst,truc,n_nav_jour]
    #plt.pie(sizes, labels=labels,  autopct='%1.4f%%', shadow=True,startangle=90,explode=(.2,.2,.2,.2,.2,.2,.2,.2,.2))
    #plt.title("nombre de validation de la semestre : {}".format(semestre.replace('.csv','')))
    #plt.show()
def jour_stats_semestre(semestre):
    dict={}
    '''fonction qui reçoit comme argument un semestre(avec l'année) et retourne un dictionnaire qui contient le nombre de validation par jour'''
    n_l,n_ma,n_me,n_je,n_ve,n_sa,n_dim=0,0,0,0,0,0,0
    with open(r'Data/'+semestre,'r') as csvfile:#adapter ton chemin jusqu'à arriver à Data
                csvreader = csv.reader(csvfile, delimiter=",")
                next(csvreader)
                for ligne in csvreader:
                    if ligne[1].lower()== 'lundi' and ligne[-1] != 'Moins de 5':
                        n_l += int(ligne[-1])
                    elif ligne[1].lower()== 'mardi' and ligne[-1] != 'Moins de 5':
                        n_ma += int(ligne[-1])
                    elif ligne[1].lower()== 'mercredi' and ligne[-1] != 'Moins de 5':
                        n_me += int(ligne[-1])
                    elif ligne[1].lower()== 'jeudi' and ligne[-1] != 'Moins de 5':
                        n_je += int(ligne[-1])
                    elif ligne[1].lower()== 'vendredi' and ligne[-1] != 'Moins de 5':
                        n_ve += int(ligne[-1])
                    elif ligne[1].lower()== 'samedi' and ligne[-1] != 'Moins de 5':
                        n_sa += int(ligne[-1])
                    elif ligne[1].lower()== 'dimanche' and ligne[-1] != 'Moins de 5':
                        n_dim += int(ligne[-1])
    dict['lundi'],dict['mardi'],dict['mercredi'],dict['jeudi'],dict['vendredi'],dict['samedi'],dict['dimanche']=n_l,n_ma,n_me,n_je,n_ve,n_sa,n_dim
    return dict

    #plt.bar(range(len(dict)), dict.values())
    #plt.xticks(range(len(dict)), dict.keys(),rotation = 60)
    #plt.title("statistiques pour {}".format(semestre.replace('.csv','')))
    #plt.show()
def jour_stats_annee(annee):#annee in {2016,2017,2018}
    '''fonction qui reçoit comme argument une année et retourne un dictionnaire qui contient le nombre de validation par jour'''
    dict={}
    n_l,n_ma,n_me,n_je,n_ve,n_sa,n_dim=0,0,0,0,0,0,0
    for num in (1,2):
        semestre='{}e-sem-{}.csv'.format(num,annee)
        dict_sem=jour_stats_semestre(semestre)
        n_l+=dict_sem['lundi']
        n_ma+=dict_sem['mardi']
        n_me+=dict_sem['mercredi']
        n_je+=dict_sem['jeudi']
        n_ve+=dict_sem['vendredi']
        n_sa+=dict_sem['samedi']
        n_dim+=dict_sem['dimanche']
    dict['lundi'],dict['mardi'],dict['mercredi'],dict['jeudi'],dict['vendredi'],dict['samedi'],dict['dimanche']=n_l,n_ma,n_me,n_je,n_ve,n_sa,n_dim
    return dict
def jour_stats():
    '''bilan des trois années(2016,2017,2018)'''
    return([jour_stats_annee(2016),jour_stats_annee(2017),jour_stats_annee(2018)])
