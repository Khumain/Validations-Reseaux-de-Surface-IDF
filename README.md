# Analyseur Validation des titres de transport
L'objectif de ce mini-projet est de developper, de manière très incrémentale, une application d'analyse et de visualisation de données avec l'écosystème python. En particulier, nous allons nous intéresser aux validations sur les réseaux de surface. Pour le semestre 2019 : nous allons déterminer le nombre de validation par titre, les détails des validations au sein des stations les plus populaires, le nombre de validation total par jour. L’évolution des données 2017, 2018, 2019 sera représentée en fonction des jours, et des titres. 

![MVP](https://st.depositphotos.com/2416623/3464/i/950/depositphotos_34644901-stock-photo-histogram-economic-rise.jpg)


## Prérequis
Sur un Terminal de Visual Studio Code, une fois que vous vous situez dans le dossier `validations-sur-les-reseaux-de-surface`, installez les différents modules nécessaires au bon fonctionnement du programme avec la commande suivante :
```bash
pip install -r requirements.txt
```
Si tous les modules ne s'installent pas correctement, essayez la commande suivante :
```bash
pip3 install -r requirements.txt
```

## Démarrage de l'application
Pour démarrer l'application, tapez dans le terminal :
```bash
python app.py
```
Il suffit alors de se rendre sur l'adresse suivante pour afficher l'application : http://127.0.0.1:8050/


## Utilisation
Dans cette partie, nous allons expliquer les différentes options que vous pouvez choisir afin d'afficher au mieux toutes les informations que vous souhaitez.

Trois critères de choix : 

-Analyse par semstre (6 semestres au total)

-Analyse par année

-Visualisation de la carte (en cours)

Pour chaque critère de choix :

-Nombre de validations hebdomadaires

-Nombre de validation par titre de transport

-Nombre de validation par trajet les plus fréquentés# Validations-Reseaux-de-Surface-IDF
