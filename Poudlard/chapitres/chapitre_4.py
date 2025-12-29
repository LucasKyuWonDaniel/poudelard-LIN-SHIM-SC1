from random import *
from Poudlard.univers.personnages import afficher_personnage

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
    proba_but = random.randint(1, 10)
    tir_reussi = proba_but >= 6
    if tir_reussi:
        if joueur_est_joueur:
            print(f"{equipe_attaque["joueurs"][0]} marque un but pour {equipe_attaque["nom"]} ! (+10 points)")
        else:
            print(f"{equipe_attaque["joueurs"][randint(1, 6)]} marque un but pour {equipe_attaque["nom"]} ! (+10 points)")
        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1
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
    for i in equipe['joueurs'] :
        joueur = i.split(" ")
        print(f"- {joueur[0]} {joueur[1]} ({joueur[2]})")

def match_quidditch(joueur, maisons):
    equipe_joueur = creer_equipe(joueur["Maison"], g, est_joueur=True, joueur=joueur)
    maison_adverse = random.choice(joueur["Maison"])
    while maison_adverse == equipe_joueur :
        maison_adverse = random.choice(joueur["Maison"])
    equipe_adverse = creer_equipe(maison_adverse, h, est_joueur=False)
    print("MATCH DE QUIDDITCH !")
    afficher_equipe_maison(equipe_joueur)
    print()
    afficher_equipe_maison(equipe_adverse)
    print()
    for tour in range(20):
        afficher_score(equipe_joueur, equipe_adverse)
        print()
        if tour % 2 == 0:
            tentative_marque(equipe_joueur, equipe_adverse, joueur_est_joueur=True)
        else:
            tentative_marque(equipe_adverse, equipe_joueur, joueur_est_joueur=False)
        if apparition_vifdor():
            print("\n*** LE VIF D'OR APPARAÎT ! ***")
            attraper_vifdor(equipe_joueur, equipe_adverse)
            break
    print("\n" + "=" * 50)
    print("FIN DU MATCH !")
    afficher_score(equipe_joueur, equipe_adverse)
    if equipe_joueur["score"] > equipe_adverse["score"]:
        print(f"\n {equipe_joueur['nom']} GAGNE LE MATCH !")
        print("Félicitations ! Vous gagnez 500 points pour votre maison !")
        joueur["Attributs"]["courage"] += 5
    else:
        print(f"\n {equipe_adverse['nom']} GAGNE LE MATCH !")
        print("Défi perdu... Votre maison perd 100 points.")
        joueur["Attributs"]["courage"] -= 2
    print("=" * 50)



def lancer_chapitre4_quidditch(joueur, maisons):
    print("\n" + "=" * 60)
    print(" CHAPITRE 4 - L'ÉPREUVE DE QUIDDITCH ")
    print("=" * 60)
    input("\n(Appuie sur Entrée pour commencer le match...) ")
    match_quidditch(joueur, maisons)
    print("\n Fin du Chapitre 4 - Quelle épreuve palpitante !")
    print("Votre maison remporte la Coupe des Quatre Maisons grâce à vos exploits !")
    input("\n(Appuie sur Entrée pour voir votre progression...) ")
    afficher_personnage(joueur)
    print("\nFélicitations sorcier ! Vous avez terminé la partie principale du jeu.")






