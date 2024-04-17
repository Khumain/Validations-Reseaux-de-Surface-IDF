import csv
import pandas as pd

# cette fonction retourne l'indice d'un element dans une liste
def indice(liste,element):
    for i in range(len(liste)):
        if liste[i]==element:
            return i

#cette fonction donne la liste des types de tickets que l'on utilise plus tard 
def cle(semestre):
    path='./Data/' + semestre
    L=[]
    with open(path,'r',encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for ligne in reader:
            #ligne[4] contient le nom des titres
            if (ligne[4] in L)==False:
                L.append(ligne[4])
    return L



def Nbre_ligne_pop(semestre):
    path='./Data/' + semestre
    d = {'Ligne':[],'Validation':[]}
    with open(path,'r',encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        for element in cle(semestre):
            d[element]=[]

        for ligne in reader:
            # On lit tout le fichier csv
            if ligne[5]=='Moins de 5':
                nombre=0
            else:
                nombre=int(ligne[5])
            if ligne[3] in d['Ligne']:
                #on regarde si on a deja rencontrer la ligne de RER
                # si oui on augmente le nombre de validation totales
                d['Validation'][-1]+=nombre
                d[ligne[4]][-1]+=nombre
            

                #Cette partie commente correspond a un code alternatif sans la fonction cles
                '''if ligne[4] in d:
                    # on regarde egalement si le type de titre de transport est present
                    # si oui on augmente le nombre de validation correspondant a ce titre
                    d[ligne[4]].append(nombre)
                else:
                    #sinon on rajoute un element au dico
                    n=len(d['Ligne'])
                    d[ligne[4]]=[]
                    for i in range(n-1):
                        d[ligne[4]].append(0)
                    d[ligne[4]].append(nombre)'''
                    
            else:
                # dans le cas ou la ligne n'est toujours pas apparue on cree des elements aux listes presentes
                d['Ligne'].append(ligne[3])
                d['Validation'].append(nombre)
                for cles in d:
                    if cles!='Ligne' and cles!='Validation' and cles!=ligne[4]:
                        #on initialise tous les types de titres a 0 a part ligne[4] 
                        d[cles].append(0)
                d[ligne[4]].append(nombre)

            # Sans la fonction cle
            '''  if ligne[4] in d:
                                d[ligne[4]].append(int(nombre))
                            else:
                                n=len(d['Ligne'])
                                d[ligne[4]]=[]
                                for i in range(n-1):
                                    d[ligne[4]].append(0)
                                d[ligne[4]].append(int(nombre))
                        for element in d:
                            if element!='Ligne' and element!='Validation':
                                if len(element)!=len(d['Ligne']):
                                    d[element].append(0)       '''
    #L=d.keys()
    #for element_bis in L:
        #print(len(d[element_bis]))
    return d

#print(pd.DataFrame(Nbre_ligne_pop('2e-sem-2017.csv')))



#Cette fonction renvoie un dictionnaire avec les memes cle que le precedent mais ne contenant que les trajets les plus frequentes
def les_plus_frequente(semestre,quantite):
    plus_frequente={}
    dico = Nbre_ligne_pop(semestre)
    #On defini les cles de plus_frequente
    for key in dico:
        plus_frequente[key]=[]
    #On se donne une liste contenant les totaux correspondant aux trajets et on la range par ordre decroissant
    validation=dico['Validation']
    validation.sort(reverse=True)
    Max=[]
    for i in range(quantite):
        #on selectionne la quantite souhaite
        Max.append(validation[i])
    for indice in range(len(dico['Validation'])):
        #on regarde 
        if dico['Validation'][indice] in Max:
            for KEY in plus_frequente:
                #on remplit le dictionnaire avec les donnees 
                plus_frequente[KEY].append(dico[KEY][indice])
    return plus_frequente
        


def tableau():
    d2016_1 = Nbre_ligne_pop('1e-sem-2016.csv')
    d2016_2 = Nbre_ligne_pop('2e-sem-2016.csv')
    d2017_1 = Nbre_ligne_pop('1e-sem-2017.csv')
    d2017_2 = Nbre_ligne_pop('2e-sem-2017.csv')
    d2018_1 = Nbre_ligne_pop('1e-sem-2018.csv')
    d2018_2 = Nbre_ligne_pop('2e-sem-2018.csv')

    return [df2016_1, df2016_2, df2017_1, df2017_2, df2018_1, df2018_2]


def maxima(nombre):
    #on definit un dictionnaire dont les cles sont les differents semestre 
    #chaque cle a pour argument un dictionnaire
    dico={'1e-sem-2016.csv': {'Ligne':[],'Validation':[]},'2e-sem-2016.csv':{'Ligne':[],'Validation':[]},'1e-sem-2017.csv':{'Ligne':[],'Validation':[]},'2e-sem-2017.csv':{'Ligne':[],'Validation':[]},'1e-sem-2018.csv':{'Ligne':[],'Validation':[]},'2e-sem-2018.csv':{'Ligne':[],'Validation':[]},'1e-sem-2019.csv':{'Ligne':[],'Validation':[]}}
    #les lignes populaires sont celles de 2016
    ligne_populaire = les_plus_frequente('1e-sem-2016.csv',nombre)['Ligne']
    for key in dico:
        sem_prov=Nbre_ligne_pop(key)
        for trajet in ligne_populaire:
            dico[key]['Ligne'].append(trajet)
            if indice(sem_prov['Ligne'],trajet)!= None:
                #On rajoute le nombre de validations correspondantes
                dico[key]['Validation'].append(sem_prov['Validation'][indice(sem_prov['Ligne'],trajet)])
            else:
                dico[key]['Validation'].append(0)
    return dico


def populaire_annee(nombre):
    d = {'Ligne':[],'Totaux':[]}
    ligne_populaire = les_plus_frequente('1e-sem-2016.csv',nombre)['Ligne']
    for trajet in ligne_populaire:
        d['Ligne'].append(trajet)
        n=0
        for sem in maxima(nombre):
            if indice(d['Ligne'],trajet) != None:               
                n += maxima(nombre)[sem]['Validation'][indice(d['Ligne'],trajet)]
        d['Totaux'].append(n)
    return d


def comparaison():
    d2016_1 = Nbre_ligne_pop('1e-sem-2016.csv')
    d2016_2 = Nbre_ligne_pop('2e-sem-2016.csv')
    d2017_1 = Nbre_ligne_pop('1e-sem-2017.csv')
    d2017_2 = Nbre_ligne_pop('2e-sem-2017.csv')
    d2018_1 = Nbre_ligne_pop('1e-sem-2018.csv')
    d2018_2 = Nbre_ligne_pop('2e-sem-2018.csv')

    Liste_trajet=[]
    for element in d2016_1['Ligne']:
        Liste_trajet.append(element)
    dico={'Trajet':[],'2016':[],'2017':[],'2018':[]}
    for i in range(len(Liste_trajet)):
        dico['Trajet'].append(Liste_trajet[i])
        dico['2016'].append(d2016_1['Validation'][i]+d2016_2['Validation'][i])
        dico['2017'].append(d2017_1['Validation'][i]+d2017_2['Validation'][i])
        dico['2018'].append(d2018_1['Validation'][i]+d2018_2['Validation'][i])
    return dico

#print(comparaison())





    

            



        






    