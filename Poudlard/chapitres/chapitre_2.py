def rencontrer_amis(joueur) :
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord... ")
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ? ")
    print("Que répondez-vous ?")
    print("1. Bien sûr, assieds-toi !")
    print("2. Désolé, je préfère voyager seul.")
    réponse1 = int(input("Votre choix :"))
    while réponse1 != 1 or réponse1 != 2 :
        réponse1 = int(input("Entrez une valeur correcte.))
    if réponse1 == 1 :
        joueur["Attributs"]["loyauté"] += 1
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable ! ")
    else :
        joueur["Attributs"]["ambition"] += 1
    
    print("Une fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    print("Que répondez-vous ?")
    print("1. Oui, j’adore apprendre de nouvelles choses ! ")
    print("2. Euh… non, je préfère les aventures aux bouquins. ")
    réponse2 = int(input("Votre choix :"))
    while réponse2 != 1 or réponse2 != 2 :
        réponse2 = int(input("Entrez une valeur correcte.))
    if réponse2 == 1 :
        joueur["Attributs"]["intelligence"] += 1
    else :
        joueur["Attributs"]["courage"] += 1
    print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour ! ")
    print("")
    print("")
    print("")
    print("")
