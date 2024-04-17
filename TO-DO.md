Objectifs:
-	Nombre de validations par titre
-	Nombre de validations par station
-	Nombre de validations par jour (plus difficile)
-	Comparer même semestre d’année en année
-	Comparer les semestres d’une seule année
-   La carte

Tableau : date, jour, numéro de semaine, nom de ligne, nom du passe, nombre de validation

Fonctionnalité 0 :
•	Accéder aux fichiers 
•	Associer à chaque date un jour (OK)
•	Créer des fonctions tests

Fonctionnalité 1 :
Données : 
•	Nombre de validation
•	Titre 
•	Station
•	Jour
Objectifs :
•	Choix du semestre et de l'année d'étude (menu déroulant)
•	Nombre de validation par titre (camembert) (OK)
•	Nombre de validation par station les plus fréquentées (tableau avec colonne Station, Total, Navigo, etc.)
•	Nombre de validation par jour (on propose une liste d’histogramme par semaine)  

Fonctionnalité 2 (comparaison 2016-2017-2018):
Données : 
•	Nombre de validation
•	Station
•	Jour
Objectifs :
•	Nombre de validation par semestre/par an pour chaque jour (histogramme comparatif sur les années)
•	Nombre de validation par titre (histogramme comparatif sur les années) 
•	Nombre de validation par station les plus fréquentées (tableau avec les colonnes Station, 2016, 2017, 2018, Moyen le plus utilisé (facultatif))



Fonctionnalité 3 :
Données : 
•	Nombre de validation
•	Station
Objectifs :
•	Créer une carte qui indique l’affluence dans les gares (avec un slider 2016 2017 2018)


Fonctions nécessaires : 
- Fonction "plateforme_choix" qui donne le choix de créer un histogramme, un camembert et de fixer des paramètres un par un avec des "input" qui donnent le choix

- Objectif 1 :
Nbre_valid_titre(semestre) --> camembert(titres)
Nbre_station_pop(semestre) --> tableau(Station,Total,Navigo,etc)
Nbre_valid_jour(semestre) --> Histogramme à 5 barres (par semaine, 7 titres)

- Objectif 2 :
Nbre_valid_annee_jour() --> histogramme à 3 barres (par jour, 3 ans)
Nbre_valid_annee_titre() --> histogramme à 3 barres (par titre, 3 ans)
Nbre_station_annee_pop() --> tableau(Station, 2016, 2017, 2018, (facultatif : moyen le plus utilisé)

