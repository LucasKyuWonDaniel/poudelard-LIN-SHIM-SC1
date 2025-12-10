from random import *
from Poudlard.utils.input_utils import charger_fichier

def apprendre_sorts(joueur, chemin_fichier="Poudlard.data.sorts.jason"):
    charger_fichier()
    sortileges=[]
    offensif = 0
    defensif = 0
    utilitaire = 0
    while offensif == 1 and defensif == 1 and utilitaire == 3:
        for i in range(5):
            sort = randint(1, 24)
            sortileges.append(sort)


def quiz_magie():
    return


