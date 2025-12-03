from Poudlard.univers.personnages import initialiser_personnage, afficher_personnage

print("Bienvenue joueur !")
input()
print("Vous vivez chez votre oncle Vernon, votre tante Pétunia et votre cousin Dudley, qui vous traitent mal depuis votre enfance, ")
print("car vous êtes orphelin après la mort mystérieuse de vos parents.")
print("Le jour de vos 11 ans, vous recevez plusieurs lettres d'une école de sorcellerie appelée Poudlard, que votre famille essaie de vous cacher. ")

def creer_personnage():
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prenom : ")
    print("Choississez vos attributs : ")
    courage = int(input("Niveau de courage (1-10) : "))
    intelligence = int(input("Niveau de intelligence (1-10) : "))
    loyaute = int(input("Niveau de loyauté (1-10) : "))
    ambition = int(input("Niveau de ambition (1-10) : "))
    attributs = {
        "courage" : courage,
        "intelligence" : intelligence,
        "loyaute" : loyaute,
        "ambition": ambition
    }
    joueur1 = initialiser_personnage(nom, prenom, attributs)
    afficher_personnage(joueur1)

print(creer_personnage())

def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scelléedu sceau de Poudlard...")
    print("« Cher élève, Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »")
    print("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?")
    print("Vous avez le choix entre aller à Poudlard ou rester chez vous")
    print("[Accepter]     [Refuser]")
    reponse = input()
    if reponse == "Accepter" :
        print("Hagrid rentre chez vous")
    if reponse == "Refuser" :
        print("Hagrid n'est pas ravie que vous refusiez et vous jette un sort.")
        print("Vous êtes mort")
        exit()
    else:
        input("Veuillez entrer une réponse correcte : ")

def rencontrer_Hagrid():
    print("Hagrid : 'Salut Harry ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.'")
    print("Voulez-vous suivre Hagrid ?")
    reponse = input("[oui]         [non]")
    if reponse == "oui" :
        print("Hagrid est ravie et vous emmène sur le chemin de Traverse.")
    if reponse == "non" :
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")
    else:
        print("Veuillez entrer une reponse correcte : ")

def acheter_fournitures():
    print("Bienvenue sur le Chemin de Traverse.")
    print("Catalogue des objets disponibles : ")
    print()
    print("1. Baguette magique  - 35 galions")
    print("2. Robe de ")
    objets_obligatoire = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]

