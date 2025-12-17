from random import *
from Poudlard.utils.input_utils import *

points_maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
}

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
    L_quiz = load_fichier(chemin_fichier)
    quiz_pose = []
    score = 0
    for i in range(1, 5) :
        quiz = choice(L_quiz)
        while quiz in quiz_pose :
                quiz = choice(L_quiz)
        reponse = demander_phrase("{}. {}".format(i, quiz["question"]))
        print(">", reponse)
        if reponse == quiz["reponse"] :
                print("Bonne réponse ! +25 points pour ta maison.")
                score += 25
        else :
                print("Mauvaise réponse. La bonne réponse était :", quiz["reponse"])
        quiz_pose.append(quiz)
    print("Score obtenu :", score, "points")
    return score
        
def lancer_chapitre_3(personnage, maisons) :
        apprendre_sorts(joueur, chemin_fichier="../data/sorts.json")
        score = quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json")
        actualiser_points_maison(points_maisons,joueur["Maison"], score)
        afficher_maison_gagnante(points_maisons)
        afficher_personnage(joueur)



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

