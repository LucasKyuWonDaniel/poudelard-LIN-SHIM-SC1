from Poudlard.chapitres.chapitre_1 import *
from Poudlard.chapitres.chapitre_2 import *
from Poudlard.chapitres.chapitre_3 import *
from Poudlard.utils.input_utils import *

def afficher_menu_principal():
    reponse = demander_choix("Que voulez-vous faire ?", ["Lancez le chapitre 1 - L'arrive dans le monde magique", "Quitter le jeu"])
    if reponse == 1:
        personnage = lancer_chapitre1()
        lancer_chapitre_2(personnage)
        lancer_chapitre_3(personnage)
    if reponse == 2:
        print("Au revoir, j'espere vous revoir bientot")
        exit()
    else :
        print("Veuillez saisir une reposne valide")

def lancer_choix_menu():
    maisons = {
        "Gryffondor" : 0,
        "Serdaigle" : 0,
        "Poufsouffler" : 0,
        "Serpentard" : 0,
    }
    while True:
        afficher_menu_principal()





