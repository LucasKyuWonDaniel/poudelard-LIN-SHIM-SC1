from random import randint, random
from Poudlard.univers.personnages import afficher_personnage
from Poudlard.utils.input_utils import *
from Poudlard.univers.Maisons import *
from Poudlard.utils.input_utils import *

def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None) :
    equipe = { 
        'nom': maison, 
        'score': 0, 
        'a_marque': 0, 
        'a_stoppe': 0, 
        'attrape_vifdor': False, 
        'joueurs': equipe_data ,
        }
    if est_joueur and joueur != None:
        L_joueurs = [joueur["Prenom"] + joueur["Nom"] + "(Attrapeur)"]
        for i in range(len(equipe_data)) :
            joueurs = equipe_data[i].split(" ")
            if joueurs[0] == joueur["Prenom"] and joueurs[1] == joueur["Nom"] :
                role = joueurs[2]
                place = i
        for i in range(len(equipe_data)) :
            if i != place :
                joueurs = equipe_data[i].split(" ")
                if joueurs[2] == "(Attrapeur)" :
                    joueurs[2] = role
                L_joueurs.append(joueurs[0] + joueurs[1] + joueurs[2])
        equipe["joueurs"] = L_joueurs
    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = randint(1, 10)
    tir_reussi = proba_but >= 6
    if tir_reussi:
        if joueur_est_joueur:
            print("{} marque un but pour {} ! (+10 points)".format(equipe_attaque["joueurs"][0],equipe_attaque["nom"] ))
        else:
            print("{} marque un but pour {} ! (+10 points)".format(equipe_attaque["joueurs"][randint(1, 6)],equipe_attaque["nom"]))
        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1
    else:
        equipe_defense["a_stoppe"] += 1
        print("{} bloque l'attaque !".format(equipe_defense["nom"]))

def apparition_vifdor():
    proba_vif = randint(1, 6)
    return proba_vif == 6

def attraper_vifdor(e1, e2):
    equipe_victorieuse = random.choice([e1, e2])
    equipe_victorieuse["score"] += 150
    equipe_victorieuse["attrape_vifdor"] = True
    print("{} attrape le Vif d'Or ! (+150 points)".format(equipe_victorieuse["nom"]))
    return equipe_victorieuse

def afficher_score(e1, e2):
    print("Score actuel :")
    print("- {} : {} points".format(e1["nom"], e1["score"]))
    print("- {} : {} points".format(e2["nom"], e2["score"]))

def afficher_equipe_maison(equipe):
    print("Équipe de {} :".format(equipe["nom"]))
    for i in equipe['joueurs'] :
        joueur = i.split(" ")
        print("- {} {} ({})".format(joueur[0], joueur[1], joueur[2]))

def match_quidditch(joueur, maisons):
    equipes = Data_quidditch
    equipe_joueur = creer_equipe(joueur["Maison"], equipes[joueur["Maison"]["joueurs"]], est_joueur=True, joueur=joueur)
    maison_adverse = random.choice(joueur["Maison"])
    while maison_adverse == equipe_joueur :
        maison_adverse = random.choice(joueur["Maison"])
    equipe_adverse = creer_equipe(maison_adverse, equipes[maison_adverse["joueurs"]], est_joueur=False)
    print("Match de Quidditch : {} vs {} !".format(joueur["Maison"], maison_adverse))
    print()
    afficher_equipe_maison(equipe_joueur)
    print()
    afficher_equipe_maison(equipe_adverse)
    print()
    print("Tu joues pour", joueur["Maison"],"en tant qu’Attrapeur")
    for tour in range(20):
        print("Tour", tour)
        tentative_marque(equipe_joueur, equipe_adverse, joueur_est_joueur=True)
        tentative_marque(equipe_adverse, equipe_joueur, joueur_est_joueur=False)
        print()
        afficher_score(equipe_joueur, equipe_adverse)
        input("Appuyez sur Entrée pour continuer")
        if apparition_vifdor():
            print("\n LE VIF D'OR APPARAÎT !")
            equipe_gagnante = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("Le Vif d’Or a été attrapé par", equipe_gagnante["nom"], "! (+150 points)")
            break
    print("FIN DU MATCH !")
    afficher_score(equipe_joueur, equipe_adverse)
    if equipe_joueur["score"] > equipe_adverse["score"]:
        print(f"\n {equipe_joueur['nom']} GAGNE LE MATCH !")
        print("Félicitations ! Vous gagnez 500 points pour votre maison !")
        joueur["Attributs"]["courage"] += 5
    else:
        print("\n {} GAGNE LE MATCH !".format(equipe_joueur["nom"]))
        print("Défi perdu... Votre maison perd 100 points.")
        joueur["Attributs"]["courage"] -= 2

def lancer_chapitre4_quidditch(joueur, maisons):
    print(" CHAPITRE 4 - L'ÉPREUVE DE QUIDDITCH ")
    input("(Appuie sur Entrée pour commencer le match...) ")
    match_quidditch(joueur, maisons)
    print("\n Fin du Chapitre 4 - Quelle épreuve palpitante !")
    maison_gagnante = afficher_maison_gagnante(maisons)
    print(maison_gagnante, "remporte la Coupe des Quatre Maisons!")
    input("\n(Appuie sur Entrée pour voir votre progression...) ")
    afficher_personnage(joueur)
    print("Félicitations sorcier ! Vous avez terminé la partie principale du jeu.")
    exit()
