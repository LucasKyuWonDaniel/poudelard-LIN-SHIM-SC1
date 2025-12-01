def initialiser_personnage(nom, prenom, attributs):
    personnage = {
        "nom": nom,
        "prenom": prenom,
        "Argent" : 100,
        "Inventaire" : [],
        "Sortilèges" : [],
        "Attributs" : attributs,
    }
    return personnage

def afficher_personnage(joueur) :
    print("Profil du personnage :")
    for cle, valeur in joueur.items():
        if cle == "Attributs" :
            print("Attributs :")
            for cle1, valeur1 in valeur.items():
                print("-", cle1, ":", valeur1)
        else :
            print(cle, ":", valeur)

def modifier_argent(joueur, montant) :
    joueur["Argent"] += montant
    return joueur

def ajouter_objet(joueur, cle, objet) :
    joueur[cle].append(objet)
    return joueur
