import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
from corpusutils.extraction import nombre_de_validation_semestre,jour_stats
from corpusutils.nbre_valid_jour import tran
from corpusutils.nbre_titre_an import nbre_titre_an
from corpusutils.Objectif_ligne import Nbre_ligne_pop

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {'Analyse semestrielle' : [{'label' : 'Nombre de validations hebdomadaires','value' : 'valid_hebdo'},
{'label' : 'Nombre de validations par titre de voyage','value' : 'valid_titre'},
{'label' : 'Nombre de validations par ligne les plus fréquentées','value' : 'valid_ligne'}], 
'Comparaison sur 3 années' : [{'label' : 'Nombre de validations hebdomadaires','value' : 'valid_annees_hebdo'},
{'label' : 'Nombre de validations par titre de voyage','value' : 'valid_annees_titre'},
{'label' : 'Nombre de validations par ligne les plus fréquentées','value' : 'valid_annees_ligne'}],
'WordCloud' : [{'label' : 'WordCloud', 'value' : 'WordCloud'}]}

semestre_options = [{'label' : '1er semestre 2016','value' : '1e-sem-2016.csv'},
{'label' : '2ème semestre 2016','value' : '2e-sem-2016.csv'},
{'label' : '1er semestre 2017','value' : '1e-sem-2017.csv'},
{'label' : '2ème semestre 2017','value' : '2e-sem-2017.csv'},
{'label' : '1er semestre 2018','value' : '1e-sem-2018.csv'},
{'label' : '2ème semestre 2018','value' : '2e-sem-2018.csv'},
{'label' : '1er semestre 2019','value' : '1e-sem-2019.csv'}]

app.layout = html.Div(children=[
    html.H1(children='Validations sur les réseaux de surface',
            style={'textAlign': 'center'}
    ),

    html.Div(children='Grâce aux données fournies dans la base Open Data Paris-Saclay, nous allons effectuer quelques analyses sur les validations en surface en Ile-de-France.', 
            style={'textAlign': 'center'}
    ),

    html.Hr(),
    
    dcc.RadioItems(
        id='first_options_dropdown',
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value='Analyse semestrielle'
    ),
    #Affiche le dropdown selon certaines conditions
    html.Div(id='first_control_container', children=[
        dcc.Dropdown(id='second_options_dropdown', searchable=False, clearable=False)
    ]),

    #Affiche le radioitem selon certaines conditions
    html.Div(id='second_control_container', children=[
    dcc.RadioItems(
        id='semestrial_option',
        options=semestre_options,
        value='1e-sem-2016.csv',
        labelStyle={'display': 'inline-block'})
    ]),

    html.Hr(),
    
    html.Div(id='table_control_container', children=[html.Table(id='table')]),

    html.Div(id='graph_control_container', children=[dcc.Graph(id='graphe')]),

    html.Div(id='image_control_container', children=[html.Img(id='image')])
])


#Si on choisit le bouton 'Carte', le dropdown disparait
@app.callback(
    Output('first_control_container', 'style'), [Input('first_options_dropdown', 'value')])
def first_toggle_container(toggle_value):
    if toggle_value == 'WordCloud':
        return {'display': 'none'}
    else:
        return {'display': 'block'}

#Si on choisit le bouton 'Analyse semestrielle', un radioitem apparait
@app.callback(
    Output('second_control_container', 'style'), [Input('first_options_dropdown', 'value')])
def second_toggle_container(toggle_value):
    if toggle_value == 'Analyse semestrielle':
        return {'display': 'block'}
    else:
        return {'display': 'none'}

#Si on choisit 'WordCloud', l'image apparait
@app.callback(
    Output('image_control_container', 'style'), [Input('first_options_dropdown', 'value')])
def image_toggle_container(toggle_value):
    if toggle_value == 'WordCloud':
        return {'display': 'block'}
    else:
        return {'display': 'none'}

#Si on choisit d'afficher des graphes, ils s'affichent
@app.callback(
    Output('graph_control_container', 'style'), 
    [Input('first_options_dropdown', 'value'),
    Input('second_options_dropdown', 'value')])
def second_toggle_container(first_value, second_value):
    if first_value == 'Analyse semestrielle':
        if second_value == 'valid_ligne' :
            return {'display': 'none'}
    elif first_value == 'WordCloud' :
        return {'display': 'none'}
    else:
        return {'display': 'block'}

#Si on choisit la table, elle s'affiche
@app.callback(
    Output('table_control_container', 'style'), 
    [Input('first_options_dropdown', 'value'),
    Input('second_options_dropdown', 'value')])
def second_toggle_container(first_value, second_value):
    if first_value == 'Analyse semestrielle':
        if second_value == 'valid_ligne' :
            return {'display': 'block'}
    else:
        return {'display': 'none'}

#Choix des données à afficher ; adapte le dropdown en fonction du choix de la première option
@app.callback(
    Output('second_options_dropdown', 'options'),
    [Input('first_options_dropdown', 'value')])
def set_first_options_dropdown(selected_option) :
    return [dico for dico in all_options[selected_option]]

@app.callback(
    Output('second_options_dropdown', 'value'),
    [Input('second_options_dropdown', 'options')])
def set_second_options_dropdown(available_options):
    return available_options[0]['value']

#Affichage du graphe, en fonction des paramètres choisis
@app.callback(
    Output('graphe', 'figure'),
    [Input('first_options_dropdown', 'value'),
     Input('second_options_dropdown', 'value'),
     Input('semestrial_option','value')])
def set_display_children(selected_first_option, selected_second_option, selected_semestre_option):
    if selected_first_option == 'Analyse semestrielle' :
        if selected_second_option == 'valid_titre' :
            donnees = nombre_de_validation_semestre(selected_semestre_option)
            return {
                'data': [go.Pie(labels = [k for k in donnees.keys()], values = [donnees[k] for k in donnees.keys()])
                ],
                'layout': {
                    'title': 'Nombre de validations par titre de voyage'
                }
            }
        else :
            donnees = tran(selected_semestre_option)
            return {
                'data': [{'x': [k for k in donnees.keys()], 'y': [donnees[k]['IMAGINE R'] for k in donnees.keys()], 'type': 'bar', 'name': 'IMAGINE R'},
                        {'x': [k for k in donnees.keys()], 'y': [donnees[k]['AMETHYSTE'] for k in donnees.keys()], 'type': 'bar', 'name': 'AMETHYSTE'},
                        {'x': [k for k in donnees.keys()], 'y': [donnees[k]['FGT'] for k in donnees.keys()], 'type': 'bar', 'name': 'FGT'},
                        {'x': [k for k in donnees.keys()], 'y': [donnees[k]['NAVIGO'] for k in donnees.keys()], 'type': 'bar', 'name': 'NAVIGO'},
                        {'x': [k for k in donnees.keys()], 'y': [donnees[k]['TST'] for k in donnees.keys()], 'type': 'bar', 'name': 'TST'},
                        {'x': [k for k in donnees.keys()], 'y': [donnees[k]['AUTRE TITRE'] for k in donnees.keys()], 'type': 'bar', 'name': 'AUTRE TITRE'},
                        {'x': [k for k in donnees.keys()], 'y': [donnees[k]['NON DEFINI'] for k in donnees.keys()], 'type': 'bar', 'name': 'NON DEFINI'},
                        {'x': [k for k in donnees.keys()], 'y': [donnees[k]['?'] for k in donnees.keys()], 'type': 'bar', 'name': '?'},
                        {'x': [k for k in donnees.keys()], 'y': [donnees[k]['NAVIGO JOUR'] for k in donnees.keys()], 'type': 'bar', 'name': 'NAVIGO JOUR'}
                ],
                'layout': {
                    'title': 'Nombre de validations hebdomadaires'
                }
            }

    elif selected_first_option == 'Comparaison sur 3 années' :
        if selected_second_option == 'valid_annees_hebdo' :
            stats_hebdo_2016, stats_hebdo_2017, stats_hebdo_2018 = jour_stats()
            return {
                'data': [{'x': [k for k in stats_hebdo_2016.keys()], 'y': [stats_hebdo_2016[k] for k in stats_hebdo_2016.keys()], 'type': 'bar', 'name': '2016'},
                        {'x': [k for k in stats_hebdo_2017.keys()], 'y': [stats_hebdo_2017[k] for k in stats_hebdo_2017.keys()], 'type': 'bar', 'name': '2017'},
                        {'x': [k for k in stats_hebdo_2018.keys()], 'y': [stats_hebdo_2018[k] for k in stats_hebdo_2018.keys()], 'type': 'bar', 'name': '2018'}
                ],
                'layout': {
                    'title': 'Nombre de validations hebdomadaires, sur 3 années'
                }
            }
        else :
            titre_2016, titre_2017, titre_2018 = nbre_titre_an(tran)
            return {
                'data': [{'x': [k for k in titre_2016.keys()], 'y': [titre_2016[k] for k in titre_2016.keys()], 'type': 'bar', 'name': '2016'},
                        {'x': [k for k in titre_2017.keys()], 'y': [titre_2017[k] for k in titre_2017.keys()], 'type': 'bar', 'name': '2017'},
                        {'x': [k for k in titre_2018.keys()], 'y': [titre_2018[k] for k in titre_2018.keys()], 'type': 'bar', 'name': '2018'}
                ],
                'layout': {
                    'title': 'Nombre de validations par titre de voyage, sur 3 années'
                }
            }

#Affichage de la table Pandas, si c'est choisi
@app.callback(
    Output('table', 'children'),
    [Input('first_options_dropdown', 'value'),
     Input('second_options_dropdown', 'value'),
     Input('semestrial_option','value')])
def set_table_children(selected_first_option, selected_second_option, selected_semestre_option):
    if selected_first_option == 'Analyse semestrielle' :
        if selected_second_option == 'valid_ligne' :
            dataframe = pd.DataFrame(Nbre_ligne_pop(selected_semestre_option))
            dataframe = dataframe.sort_values('Validation', ascending = False)
            max_rows = 25
            return (
                # Header
                [html.Tr([html.Th(col) for col in dataframe.columns])] +

                # Body
                [html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ]) for i in range(max_rows)]
            )

@app.callback(
    Output('image', 'src'),
    [Input('first_options_dropdown', 'value'),
     Input('second_options_dropdown', 'value'),
     Input('semestrial_option','value')])
def set_image_children(selected_first_option, selected_second_option, selected_semestre_option):
    if selected_first_option == 'WordCloud' :
        return app.get_asset_url ('buscloud.png')

if __name__ == '__main__':
    app.run_server(debug=True)