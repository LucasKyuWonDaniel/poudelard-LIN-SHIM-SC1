from Poudlard.utils.input_utils import *
from Poudlard.univers.Maisons import *
from Poudlard.univers.personnages import *

def rencontrer_amis(joueur) :
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord... ")
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ? ")
    L_réponse1 = ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."]
    réponse1 = demander_choix("Que répondez-vous ?", L_réponse1)
    if réponse1 == 1 :
        joueur["Attributs"]["loyauté"] += 1
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable ! ")
    else :
        joueur["Attributs"]["ambition"] += 1
        print("Ron : — Pas de probleme, mon pote !")
    
    print("Une fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    L_réponse2 = ["Oui, j’adore apprendre de nouvelles choses !", "Euh… non, je préfère les aventures aux bouquins."]
    réponse2 = demander_choix("Que répondez-vous ?", L_réponse2)
    if réponse2 == 1 :
        joueur["Attributs"]["intelligence"] += 1
        print("Hermione : — Super! Dans Histoire de la Magie, quel événement majeur Bathilda Tourdesac identifie-t-elle comme la cause première de l’adoption du Code International du Secret Magique ?")
        input("Votre réponse :")
    else :
        joueur["Attributs"]["courage"] += 1
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour ! ")
    
    print("Puis un garçon blond entre avec un air arrogant.")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    L_réponse3 = ["Je lui serre la main poliment.", "Je l’ignore complètement.", "Je lui réponds avec arrogance."]
    réponse3 = demander_choix("Comment réagissez-vous ?", L_réponse3)
    if réponse3 == 1 :
        joueur["Attributs"]["ambition"] += 1
        print("Drago : — HaHaHa! ")
    elif réponse3 == 2 :
        joueur["Attributs"]["loyauté"] += 1
        print("Drago fronce les sourcils, vexé : — Tu le regretteras !")
    else :
        joueur["Attributs"]["courage"] += 1
        print("Drago : — Qui te crois tu ! ")
    print("Le train continue sa route. Le château de Poudlard se profile à l’horizon... ")
    print("Tes choix semblent déjà en dire long sur ta personnalité !")
    print("Tes attributs mis à jour :", joueur["Attributs"])

def mot_de_bienvenue() :
    print("Bienvenue à Poudlard, jeune sorcier !")
    print("Je suis le professeur Dumbledore, et je suis ravi", end = " ")
    print("de t’accueillir pour cette nouvelle aventure magique.")
    print("Prépare-toi à faire des choix importants...")
    input("\n(Appuie sur Entrée pour continuer...) ")

def ceremonie_repartition(joueur) :
    print("La cérémonie de répartition commence dans la Grande Salle...")
    print("Le Choixpeau magique t’observe longuement avant de poser ses questions :")
    maison_gagnante = repartition_maison(joueur, questions)
    joueur["Maison"] = maison_gagnante
    print("Le Choixpeau s’exclame :", maison_gagnante, "!!!")
    print("Tu rejoins les élèves de", maison_gagnante, "sous les acclamations !")

def installation_salle_commune(joueur) :
    maison = load_fichier("data/maisons.json")
    print("Vous suivez les préfets à travers les couloirs du château...")
    for cle1, valeur1 in maison.items() :
        if cle1 == joueur["maison"] :
            print(valeur1["emoji"], valeur1["description"])
            print(valeur1["message_installation"])
            print("Les couleurs de votre maison : {}, {}".format(valeur1["couleurs"][0], valeur1["couleurs"][1]))
            joueur["Traits"] = valeur1["traits"]
            for cle2, valeur2 in valeur1["bonus_attributs"].items() :
                joueur["Attributs"][cle2] += valeur2

def lancer_chapitre_2(personnage) :
    rencontrer_amis(personnage)
    mot_de_bienvenue()
    ceremonie_repartition(personnage)
    installation_salle_commune(personnage)
    afficher_personnage(personnage)
    print("Fin du chapitre 2 !")
    print("Les cours à Poudlard commenceront dès demain.")
    print("Prépare-toi pour une nouvelle aventure magique !")

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


lancer_chapitre_2(j1)





