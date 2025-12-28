from random import *

def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None) :
    equipe = { 
        'nom': maison, 
        'score': 0, 
        'a_marque': 0, 
        'a_stoppe': 0, 
        'attrape_vifdor': False, 
        'joueurs': equipe_data ,
        }
    if est_joueur == True and joueur != None:
        L_joueurs = [joueur["Prenom"] + joueur["Nom"] + "(Attrapeur)"]
        for i in range(len(equipe_data)) :
            joueur = equipe_data[i].split(" ")
            if joueur[0] == joueur["Prenom"] and joueur[1] == joueur["Nom"] :
                role = joueur[2]
                place = i

        for i in range(len(equipe_data)) :
            if i != place :
                joueur = equipe_data[i].split(" ")
                if joueur[2] == (Attrapeur) :
                    equipe_data[i] = joueur[0] + joueur[1] + role
                L_joueur.append(equipe_data[i])
        equipe["joueurs"] = L_joueurs
    return equipe

def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False) :
    proba_but = randint(1, 10)
    if proba_but >= 6 :
        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1
        if  joueur_est_joueur=True :
            print("{} marque un but pour {}!(+10 points)".format(equipe_attaque["joueurs"][0], equipe_attaque["nom"]))
        else :
            print("{} marque un but pour {}!(+10 points)".format(equipe_attaque["joueurs"][randint(1, 6)], equipe_attaque["nom"]))
    else :
        equipe_attaque["a_stoppe"] += 1
        print("{} bloque l’attaque!".format(equipe_defense["nom"]))

def apparition_vifdor() :
    if randint(1, 6) == 6 :
        return True
    else :
        return False

