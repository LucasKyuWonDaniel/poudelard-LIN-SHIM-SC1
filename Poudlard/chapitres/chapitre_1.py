from Poudlard.univers.personnages import initialiser_personnage, afficher_personnage
from Poudlard.utils.input_utils import *


def introduction():
    print("\n Bienvenue joueur !")
    print("\n Vous vivez chez votre oncle Vernon, votre tante Pétunia et votre cousin Dudley, qui vous traitent mal depuis votre enfance, ")
    print("car vous êtes orphelin après la mort mystérieuse de vos parents.")
    print("Le jour de vos 11 ans, vous recevez plusieurs lettres d'une école de sorcellerie appelée Poudlard, que votre famille essaie de vous cacher. ")


def creer_personnage():
    nom = demander_texte("Entrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prénom de votre personnage : ")
    print("Choisissez vos attributs : ")
    courage = demander_nombre("Niveau de courage (1-10) : ", 1, 10)
    intelligence = demander_nombre("Niveau d'intelligence (1-10) : ", 1, 10)
    loyaute = demander_nombre("Niveau de loyauté (1-10) : ", 1, 10)
    ambition = demander_nombre("Niveau d'ambition (1-10) : ", 1, 10)
    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyauté": loyaute,
        "ambition": ambition
    }
    joueur = initialiser_personnage(nom, prenom, attributs)
    print("")
    afficher_personnage(joueur)
    return joueur


def recevoir_lettre():
    print("\n Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...")
    print("« Cher élève, Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »")
    print("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?")
    print("1. Oui, bien sûr !")
    print("2. Non, je préfère rester avec l’oncle Vernon...")
    choix = demander_nombre("Votre choix : ", 1, 2)
    if choix == 1:
        print("\n Vous acceptez de partir pour Poudlard. L’aventure continue !")
    else:
        print("\n Vous refusez d'aller à Poudlard.")
        print("Hagrid n'est pas satisfait de votre reponse et vous jette un sort ")
        print("Vous êtes morts")
        exit()


def rencontrer_Hagrid():
    print("\n Hagrid : 'Salut Harry ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.'")
    reponse = demander_choix("Voulez-vous suivre Hagrid ?", ["oui","non"])
    if reponse == 1:
        print("Hagrid est ravi et vous emmène sur le Chemin de Traverse.")
    elif reponse == 2:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui !")
    else:
        print("Réponse invalide, Hagrid vous entraîne quand même avec lui !")


def acheter_fournitures(personnage):
    print("\n Bienvenue sur le Chemin de Traverse !")
    objets = ["Baguette magique", "Robe de sorcier", "Chaudron en étain",
              "Manuel de potions", "Plume magique", "Livre enchanté",
              "Balance de cuivre", "Cape d'invisibilité"]
    prix =   [35,20,15,25,5,30,10,100]
    objets_obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    while len(objets_obligatoires) > 0:
        print("\n Catalogue des objets disponibles :")
        for i in range(len(objets)):
            print("{0}. {1} - {2} galions".format(i + 1, objets[i], prix[i]))
        print("Vous avez", personnage["Argent"], "galions.")
        print("Objets obligatoires restants :", objets_obligatoires)
        choix_objet = demander_nombre("\n Quels objets voulez-vous acheter? : ", 1,8)
        nom_objet_achete = objets[choix_objet-1]
        cout = prix[choix_objet-1]
        if personnage["Argent"] < cout:
            print("Vous n'avez pas assez d'argent. Fin du jeu.")
            exit()
        personnage["Argent"] -= cout
        personnage["Inventaire"].append(objets[choix_objet-1])
        print("Vous avez acheté : {} (-{} galions).".format(objets[choix_objet - 1], cout))
        if objets[choix_objet-1] in objets_obligatoires:
            objets_obligatoires.remove(objets[choix_objet-1])
    print("Tous les objets obligatoires ont été achetés !")
    animaux = ["Chouette", "Chat", "Rat", "Crapaud"]
    prix_animaux = [20, 15, 10, 5]
    print("Il est temps de choisir votre animal de compagnie pour Poudlard !")
    print("Vous avez", personnage["Argent"], "galions.")
    for i in range(len(animaux)):
        print("{0}. {1} - {2} galions".format(i + 1, animaux[i], prix_animaux[i]))
    choix_animal = int(input("Quel animal voulez-vous ? :"))
    animal = animaux[choix_animal-1]
    cout_animal = prix_animaux[choix_animal-1]
    if personnage["Argent"] < cout_animal:
        print("Vous n'avez pas assez d'argent pour cet animal. Fin du jeu.")
        exit()
    personnage["Argent"] -= cout_animal
    personnage["Inventaire"].append(animal)
    print("Vous avez choisi : {} (-{} galions).".format(animal, cout_animal))
    print("Tous les objets obligatoires ont été achetés avec succès ! Voici votre inventaire final :", personnage["Inventaire"])
    afficher_personnage(personnage)


def lancer_chapitre1():
    introduction()
    joueur1 = creer_personnage()
    recevoir_lettre()
    rencontrer_Hagrid()
    acheter_fournitures(joueur1)
    print("Fin du chapitre 1! Votre aventure commence à Poudlard...")
    return joueur1





