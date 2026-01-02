import random
from random import randint
from Poudlard.univers.personnages import afficher_personnage
from Poudlard.utils.input_utils import *
from Poudlard.univers.Maisons import *
from Poudlard.utils.input_utils import *


def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {
        'nom': maison,
        'score': 0,
        'a_marque': 0,
        'a_stoppe': 0,
        'attrape_vifdor': False,
        'joueurs': equipe_data,
    }
    if est_joueur and joueur is not None:
        L_joueurs = [joueur["prenom"] + " " + joueur["nom"] + " (Attrapeur)"]
        place_attrapeur = -1
        for i in range(len(equipe_data)):
            if "(Attrapeur)" in equipe_data[i]:
                place_attrapeur = i
                break
        for i in range(len(equipe_data)):
            if i != place_attrapeur:
                L_joueurs.append(equipe_data[i])
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
    for i in equipe['joueurs']:
        joueur = i.split(" (")
        nom = joueur[0]
        role = ""
        if len(joueur) > 1:
            role_list = joueur[1].split(")")
            role = role_list[0]
        print("- {} ({})".format(nom, role))


def match_quidditch(joueur, maisons):
    equipes = Data_quidditch
    equipe_joueur = equipe_joueur = creer_equipe(joueur["Maison"], equipes[joueur["Maison"]]["joueurs"], est_joueur=True, joueur=joueur)
    maisons_possibles = [m for m in equipes.keys() if m != joueur["Maison"]]
    maison_adverse = random.choice(maisons_possibles)
    while maison_adverse == equipe_joueur :
        maison_adverse = random.choice(joueur["Maison"])
    equipe_adverse = creer_equipe(maison_adverse,equipes[maison_adverse]["joueurs"],est_joueur=False)
    print("Match de Quidditch : {} vs {} !".format(joueur["Maison"], maison_adverse))
    print()
    afficher_equipe_maison(equipe_joueur)
    print()
    afficher_equipe_maison(equipe_adverse)
    print()
    print("Tu joues pour", joueur["Maison"],"en tant qu’Attrapeur")
    for tour in range(20):
        print("")
        print("Tour", tour)
        tentative_marque(equipe_joueur, equipe_adverse, joueur_est_joueur=True)
        tentative_marque(equipe_adverse, equipe_joueur, joueur_est_joueur=False)
        print()
        afficher_score(equipe_joueur, equipe_adverse)
        input("\n Appuyez sur Entrée pour continuer")
        if apparition_vifdor():
            print("\n LE VIF D'OR APPARAÎT !")
            equipe_gagnante = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("Le Vif d’Or a été attrapé par", equipe_gagnante["nom"], "! (+150 points)")
            break
    print("FIN DU MATCH !")
    afficher_score(equipe_joueur, equipe_adverse)
    if equipe_joueur["score"] > equipe_adverse["score"]:
        print("\n {} GAGNE LE MATCH !".format(equipe_joueur["nom"]))
        print("Félicitations ! Vous gagnez 500 points pour votre maison !")
        actualiser_points_maison(maisons, equipe_joueur["nom"], 500)
        joueur["Attributs"]["courage"] += 5
    else:
        print("\n {} GAGNE LE MATCH !".format(equipe_adverse["nom"]))
        actualiser_points_maison(maisons, equipe_adverse["nom"], 500)
        print("Défi perdu... Votre maison perd 100 points.")
        actualiser_points_maison(maisons, equipe_joueur["nom"], -100)
        joueur["Attributs"]["courage"] -= 2


def lancer_chapitre4_quidditch(joueur, maisons):
    print(" CHAPITRE 4 - L'ÉPREUVE DE QUIDDITCH ")
    input("(Appuie sur Entrée pour commencer le match...) ")
    match_quidditch(joueur, maisons)
    print("\n Fin du Chapitre 4 - Quelle épreuve palpitante !")
    maison_gagnante = afficher_maison_gagnante(maisons)
    print("")
    print(maison_gagnante, "remporte la Coupe des Quatre Maisons!")
    input("\n(Appuie sur Entrée pour voir votre progression...) ")
    afficher_personnage(joueur)
    print("\nFélicitations sorcier ! Vous avez terminé la partie principale du jeu.")
    exit()



