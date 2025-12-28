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
                L_joueur.append(equipe_data[i])
                
            if joueur[0] != joueur["Prenom"] or joueur[1] != joueur["Nom"] :
                L_joueur.append(i)
        equipe["joueurs"] = L_joueurs
    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1, 10)
    tir_reussi = proba_but >= 6
    if tir_reussi:
        if joueur_est_joueur:
            buteur = equipe_attaque["joueurs"][0]
        else:
            buteur = random.choice(equipe_attaque["joueurs"])
        nom_buteur = buteur["nom"]
        role_buteur = buteur["role"]
        nom_equipe = equipe_attaque["nom"]
        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1
        print(f"{nom_buteur} ({role_buteur}) marque un but pour {nom_equipe} ! (+10 points)")
    else:
        equipe_defense["a_stoppe"] += 1
        print(f"{equipe_defense['nom']} bloque l'attaque !")

def apparition_vifdor():
    proba_vif = random.randint(1, 6)
    return proba_vif == 6

def attraper_vifdor(e1, e2):
    equipe_victorieuse = random.choice([e1, e2])
    equipe_victorieuse["score"] += 150
    equipe_victorieuse["attrape_vifdor"] = True
    print(f"{equipe_victorieuse['nom']} attrape le Vif d'Or ! (+150 points)")
    return equipe_victorieuse

def afficher_score(e1, e2):
    print("Score actuel :")
    print(f"- {e1['nom']} : {e1['score']} points")
    print(f"- {e2['nom']} : {e2['score']} points")

def afficher_equipe_maison(equipe):
    print(f"Équipe de {equipe['nom']} :")
    for joueur in equipe['joueurs']:
        print(f"- {joueur['nom']} ({joueur['role']})")



