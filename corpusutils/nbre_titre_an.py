def nbre_titre_an(tran):
    #fonction qui renvoie 3 dicos (1 pour chaque année) avec le nombre de validations pour chaque titre de transport
    dicti1 = list(tran('2e-sem-2016.csv').values())
    dicti2 = list(tran('2e-sem-2016.csv').values())
    dicti3 = list(tran('1e-sem-2017.csv').values())
    dicti4 = list(tran('2e-sem-2017.csv').values())
    dicti5 = list(tran('1e-sem-2018.csv').values())
    dicti6 = list(tran('2e-sem-2018.csv').values())

    #print(tran('2e-sem-2018.csv').values())
    #print((tran('2e-sem-2016.csv').values()[1]).keys())

    Dicti1 ={'IMAGINE R': 0, 'NON DEFINI' : 0, 'AUTRE TITRE':0, 'FGT':0, 'NAVIGO':0, 'AMETHYSTE': 0, 'TST':0,'?':0,'NAVIGO JOUR':0}
    Dicti2 ={'IMAGINE R': 0, 'NON DEFINI' : 0, 'AUTRE TITRE':0, 'FGT':0, 'NAVIGO':0, 'AMETHYSTE': 0, 'TST':0,'?':0,'NAVIGO JOUR':0}
    Dicti3 ={'IMAGINE R': 0, 'NON DEFINI' : 0, 'AUTRE TITRE':0, 'FGT':0, 'NAVIGO':0, 'AMETHYSTE': 0, 'TST':0,'?':0,'NAVIGO JOUR':0}
    #print((tran('2e-sem-2016.csv').values()))
    for key in dicti1[1].keys():
        for i in range(7):
            Dicti1[key] += dicti1[i][key] + dicti2[i][key] 
            Dicti2[key] += dicti3[i][key] + dicti4[i][key]
            Dicti3[key] += dicti5[i][key] + dicti6[i][key]

    return Dicti1,Dicti2,Dicti3

''' # clé après clé, on complète le dictionnaire de l'année 1, 2, puis 3 (ie 2016 2017 2018)
Dicti1['IMAGINE R'] = dicti1[1][0] + dicti2[1][0] 
Dicti2['IMAGINE R'] = dicti3[1][0] + dicti4[1][0]
Dicti3['IMAGINE R'] = dicti5[1][0] + dicti6[1][0]

Dicti1['NON DEFINI'] = dicti1[1][1] + dicti2[1][1] 
Dicti2['NON DEFINI'] = dicti3[1][1] + dicti4[1][1]
Dicti3['NON DEFINI'] = dicti5[1][1] + dicti6[1][1]

Dicti1['AUTRE TITRE'] = dicti1[1][2] + dicti2[1][2] 
Dicti2['AUTRE TITRE'] = dicti3[1][2] + dicti4[1][2]
Dicti3['AUTRE TITRE'] = dicti5[1][2] + dicti6[1][2]

Dicti1['FGT'] = dicti1[1][3] + dicti2[1][3] 
Dicti2['FGT'] = dicti3[1][3] + dicti4[1][3]
Dicti3['FGT'] = dicti5[1][3]+dicti6[1][3]

Dicti1['NAVIGO'] = dicti1[1][4] + dicti2[1][4]
Dicti2['NAVIGO'] = dicti3[1][4] + dicti4[1][4]
Dicti3['NAVIGO'] = dicti5[1][4]+dicti6[1][4]

Dicti1['TST'] = dicti1[1][5] + dicti2[1][5] 
Dicti2['TST'] = dicti3[1][5] + dicti4[1][5]
Dicti3['TST'] = dicti5[1][5]+dicti6[1][5]

Dicti1['?'] = dicti1[1][6] + dicti2[1][6]
Dicti2['?'] = dicti3[1][6] + dicti4[1][6]
Dicti3['?'] = dicti5[1][6]+dicti6[1][6]

Dicti1['NAVIGO JOUR'] = dicti1[1][7] + dicti2[1][7] 
Dicti2['NAVIGO JOUR'] = dicti3[1][7] + dicti4[1][7]
Dicti3['NAVIGO JOUR'] = dicti5[1][7]+dicti6[1][7]'''

    

#print(nbre_titre_an())
