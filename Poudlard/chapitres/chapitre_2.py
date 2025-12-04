def rencontrer_amis(joueur) :
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord... ")
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ? ")
    print("Que répondez-vous ?")
    print("1. Bien sûr, assieds-toi !")
    print("2. Désolé, je préfère voyager seul.")
    réponse1 = int(input("Votre choix :"))
    while réponse1 != 1 and réponse1 != 2 :
        réponse1 = int(input("Entrez une valeur correcte."))
    if réponse1 == 1 :
        joueur["Attributs"]["loyauté"] += 1
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable ! ")
    else :
        joueur["Attributs"]["ambition"] += 1
        print("Ron : — Pas de probleme, mon pote !")
    
    print("Une fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    print("Que répondez-vous ?")
    print("1. Oui, j’adore apprendre de nouvelles choses ! ")
    print("2. Euh… non, je préfère les aventures aux bouquins. ")
    réponse2 = int(input("Votre choix :"))
    while réponse2 != 1 and réponse2 != 2 :
        réponse2 = int(input("Entrez une valeur correcte."))
    if réponse2 == 1 :
        joueur["Attributs"]["intelligence"] += 1
        print("Hermione : — Super! Dans Histoire de la Magie, quel événement majeur Bathilda Tourdesac identifie-t-elle comme la cause première de l’adoption du Code International du Secret Magique ?")
        input("")
    else :
        joueur["Attributs"]["courage"] += 1
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour ! ")
    
    print("Puis un garçon blond entre avec un air arrogant.")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    print("Comment réagissez-vous ? ")
    print("1. Je lui serre la main poliment.")
    print("2. Je l’ignore complètement.")
    print("3. Je lui réponds avec arrogance.")
    réponse3 = int(input("Votre choix :"))
    while réponse3 != 1 and réponse3 != 2 :
        réponse3 = int(input("Entrez une valeur correcte."))
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
    print("Tes attributs mis à jour :", joueur["Atributs"])



