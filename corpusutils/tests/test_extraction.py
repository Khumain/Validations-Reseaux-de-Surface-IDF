from corpusutils.extraction import *


def test_nombre_de_validation_semestre():
    assert nombre_de_validation_semestre('2e-sem-2018.csv')=={'IMAGINE R': 195800, 'NON DEFINI': 2128, 'AUTRE TITRE': 100940, 'FGT': 177845, 'NAVIGO': 193873, 'AMETHYSTE': 164911, 'TST': 175972, '?': 46674, 'NAVIGO JOUR': 0}
    
def test_jour_stats_semestre():
    assert jour_stats_semestre('2e-sem-2018.csv')=={'lundi': 87830462, 'mardi': 88334172, 'mercredi': 87926046, 'jeudi': 88481158, 'vendredi': 89275952, 'samedi': 51042282, 'dimanche': 32033423}
   
def test_jour_stats_annee():
    assert jour_stats_annee(2018) == {'lundi': 179046307, 'mardi': 184532393, 'mercredi': 185655374, 'jeudi': 186089505, 'vendredi': 189815138, 'samedi': 109074706, 'dimanche': 64478503}
    
def test_jour_stats():
    assert jour_stats()==[{'lundi': 163976769, 'mardi': 172767139, 'mercredi': 171703381, 'jeudi': 168846685, 'vendredi': 167120013, 'samedi': 99242713, 'dimanche': 57530383}, {'lundi': 162351978, 'mardi': 180101367, 'mercredi': 176655578, 'jeudi': 178972741, 'vendredi': 177552227, 'samedi': 101881920, 'dimanche': 60568938}, {'lundi': 179046307, 'mardi': 184532393, 'mercredi': 185655374, 'jeudi': 186089505, 'vendredi': 189815138, 'samedi': 109074706, 'dimanche': 64478503}]
    """
    filename = r"Data\1e-semestre-2019.csv"
    # When
    ligne_1 = to_dict(filename)[0]
    #Then
    assert ligne_1 == {}
    # Given
    filename1 = r"Data\1e-semestre-2018.csv"
    # When
    ligne_1 = to_dict(filename1)[2]
    #Then
    assert annotations1 == {}
"""
