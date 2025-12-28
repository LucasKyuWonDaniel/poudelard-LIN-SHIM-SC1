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
                if 
                L_joueur.append(equipe_data[i])
                
            if joueur[0] != joueur["Prenom"] or joueur[1] != joueur["Nom"] :
                L_joueur.append(i)
        equipe["joueurs"] = L_joueurs
    return equipe
