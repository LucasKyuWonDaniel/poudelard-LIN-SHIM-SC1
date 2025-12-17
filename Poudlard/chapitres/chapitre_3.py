from random import *
from Poudlard.utils.input_utils import *

def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    print("Tu commences tes cours de magie à Poudlard...")
    sorts = load_fichier(chemin_fichier)
    sortileges=[]
    offensif = 0
    defensif = 0
    utilitaire = 0
    while offensif != 1 and defensif != 1 and utilitaire != 3:
        sort = randint(0, 24)
        if sorts[sort]["type"] == "Offenssif" and offensif == 0 :
            print("Tu viens d'apprendre le sortilège : {} ({})".format(sorts[sort]["nom"], sorts[sort]["type"]))
            sortileges.append(sorts[sort]["nom"])
            offensif += 1
            input("Appuie sur Entrée pour continuer...")
        elif sorts[sort]["type"] == "Défensif" and defensif == 0 :
            print("Tu viens d'apprendre le sortilège : {} ({})".format(sorts[sort]["nom"], sorts[sort]["type"]))
            sortileges.append(sorts[sort]["nom"])
            defensif += 1
            input("Appuie sur Entrée pour continuer...")
        elif sorts[sort]["type"] == "Unilitaire" and utilitaire != 3 :
            print("Tu viens d'apprendre le sortilège : {} ({})".format(sorts[sort]["nom"], sorts[sort]["type"]))
            sortileges.append(sorts[sort]["nom"])
            utilitaire += 1
            input("Appuie sur Entrée pour continuer...")
    print("")
    print("Tu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")
    for i in range(5) :
        for i in range(24) :
                 if sorts[i]["nom"] == joueur["Sortilèges"][i] :
                     type = sorts[i]["type"]
        for i in range(24) :
                 if sorts[i]["nom"] == joueur["Sortilèges"][i] :
                     description = sorts[i]["description"]
        print("- {} ({}) : {}".format(joueur["Sortilèges"][i], type, description))


def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json") :
    print("Bienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.")

j1 = {
    "Nom" : "SHIM" ,
    "Prenom" : "Daniel" ,
    "Argent" : 100,
    "Inventaire" : ["couteau"],
    "Sortilèges" : ["feu"] ,
    "Attributs" : {"courage" : 3 ,
    "intelligence" : 8 ,
    "loyauté" : 6 ,
    "ambition" : 4
    }
    }

