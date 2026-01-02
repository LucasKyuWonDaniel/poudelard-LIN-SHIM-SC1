from random import *
from Poudlard.utils.input_utils import *
from Poudlard.univers.Maisons import  *
from Poudlard.univers.personnages import  *


def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    print("\n Tu commences tes cours de magie à Poudlard...")
    sorts = SORTS_DATA
    sortileges=[]
    offensif = 0
    defensif = 0
    utilitaire = 0
    while offensif != 1 or defensif != 1 or utilitaire != 3:
        sort = randint(0, 23)
        while sorts[sort]["nom"] in sortileges :
            sort = randint(0, 23)
        if sorts[sort]["type"] == "Offensif" and offensif != 1 :
            print("\n Tu viens d'apprendre le sortilège : {} ({})".format(sorts[sort]["nom"], sorts[sort]["type"]))
            sortileges.append(sorts[sort]["nom"])
            offensif += 1
            input("Appuie sur Entrée pour continuer...")
        elif sorts[sort]["type"] == "Défensif" and defensif != 1 :
            print("\n Tu viens d'apprendre le sortilège : {} ({})".format(sorts[sort]["nom"], sorts[sort]["type"]))
            sortileges.append(sorts[sort]["nom"])
            defensif += 1
            input("Appuie sur Entrée pour continuer...")
        elif sorts[sort]["type"] == "Utilitaire" and utilitaire != 3 :
            print("\n Tu viens d'apprendre le sortilège : {} ({})".format(sorts[sort]["nom"], sorts[sort]["type"]))
            sortileges.append(sorts[sort]["nom"])
            utilitaire += 1
            input("Appuie sur Entrée pour continuer...")
    print("")
    print("Tu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")
    joueur["Sortilèges"] = sortileges
    for i in sortileges :
        for j in range(24) :
            if sorts[j]["nom"] == i :
                type = sorts[j]["type"]
        for l in range(24) :
           if sorts[l]["nom"] == i :
                description = sorts[l]["description"]
        print("- {} ({}) : {}".format(i, type, description))


def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json") :
    print("\n Bienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.")
    L_quiz = QUIZ_DATA
    quiz_pose = []
    score = 0
    for i in range(1, 5) :
        quiz = choice(L_quiz)
        while quiz in quiz_pose :
                quiz = choice(L_quiz)
        reponse = demander_texte("{}. {}".format(i, quiz["question"]))
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
        apprendre_sorts(personnage, chemin_fichier="../data/sorts.json")
        score = quiz_magie(personnage, chemin_fichier="../data/quiz_magie.json")
        actualiser_points_maison(maisons,personnage["Maison"], score)
        print("La maison actuellement en tête est :", afficher_maison_gagnante(maisons))
        afficher_personnage(personnage)

