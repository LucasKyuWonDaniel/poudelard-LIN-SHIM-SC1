from Poudlard.chapitres.chapitre_1 import *
from Poudlard.chapitres.chapitre_2 import *
from Poudlard.chapitres.chapitre_3 import *
from Poudlard.chapitres.chapitre_4 import *
from Poudlard.utils.input_utils import *


def afficher_menu_principal():
    reponse = demander_choix("Que voulez-vous faire ?", [
        "Lancez le chapitre 1 - L'arrivée dans le monde magique",
        "Quitter le jeu"
    ])
    maisons = {
        "Gryffondor": 0,
        "Serdaigle": 0,
        "Poufsouffle": 0,
        "Serpentard": 0,
    }
    if reponse == 1:
        personnage = lancer_chapitre1()
        lancer_chapitre_2(personnage)
        lancer_chapitre_3(personnage, maisons)
        lancer_chapitre4_quidditch(personnage, maisons)
        return
    elif reponse == 2:
        print("Au revoir, j'espère vous revoir bientôt !")
        exit()
    else:
        print("Veuillez saisir une réponse valide.")
        afficher_menu_principal()


def lancer_choix_menu():
    while True:
        afficher_menu_principal()






