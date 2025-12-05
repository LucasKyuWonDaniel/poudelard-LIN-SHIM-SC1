from Poudlard.utils.input_utils import *

def rencontrer_amis(joueur) :
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord... ")
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ? ")
    print("Que répondez-vous ?")
    L_réponse1 = ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."]
    demander_choix("Votre choix :", L_réponse1)
    if réponse1 == 1 :
        joueur["Attributs"]["loyauté"] += 1
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable ! ")
    else :
        joueur["Attributs"]["ambition"] += 1
        print("Ron : — Pas de probleme, mon pote !")
    
    print("Une fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    print("Que répondez-vous ?")
    L_réponse2 = ["Oui, j’adore apprendre de nouvelles choses !", "Euh… non, je préfère les aventures aux bouquins."]
    demander_choix("Votre choix :", L_réponse2)
    if réponse2 == 1 :
        joueur["Attributs"]["intelligence"] += 1
        print("Hermione : — Super! Dans Histoire de la Magie, quel événement majeur Bathilda Tourdesac identifie-t-elle comme la cause première de l’adoption du Code International du Secret Magique ?")
        input("Votre réponse :")
    else :
        joueur["Attributs"]["courage"] += 1
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour ! ")
    
    print("Puis un garçon blond entre avec un air arrogant.")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    print("Comment réagissez-vous ? ")
    L_réponse3 = ["Je lui serre la main poliment.", "Je l’ignore complètement.", "Je lui réponds avec arrogance."]
    demander_choix("Votre choix :", L_réponse3)
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







