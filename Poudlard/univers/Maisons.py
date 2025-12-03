def actualiser_points_maison(maisons, nom_maison, points) :
  if nom_maison in maisons :
    maisons[nom_maison] += points
    print (nom_maison, ":", maisons[nom_maison])
  else :
    return " la maison est introuvable"

def afficher_maison_gagnante(maisons) :
    L_maison_gagnante = []
    max = maisons["Gryffondor"]
    for valeur in maisons.values() :
        if max < valeur :
            max = valeur
    for cle in maisons.keys() :
        if maisons[cle] == max :
            L_maison_gagnante.append(cle)
    if len(L_maison_gagnante) > 1 :
        for i in range(len(L_maison_gagnante)) :
            print(L_maison_gagnante[i])
        print("Ces maisons sont ex æquo.")
        maison_gagnante = str(input("Quelles maisons voulez-vous choisir ?"))
        return maison_gagnante
    else :
        return L_maison_gagnante[0]

def repartition_maison(joueur, questions) :
    score_maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }
    for cle, valeur in joueur["Attributs"].items() :
        if cle == "courage" :
            actualiser_points_maison(score_maisons, "Gryffondor", valeur * 2)
        elif cle == "Ambition" :
            actualiser_points_maison(score_maisons, "Serpentard", valeur * 2)
        elif cle == "Loyauté" :
            actualiser_points_maison(score_maisons, "Poufsouffle", valeur * 2)
        else :
            actualiser_points_maison(score_maisons, "Serdaigle", valeur * 2)
    for i in questions :
        for j in range(len(i)):
            if j == 0 :
                print(i[j])
            elif j == 1 :
                for k in range(1, len(i[j]) + 1):
                    print(k + "." + " " + i[j][k - 1])
            else :
                réponse = int(input("Ton choix : "))
                actualiser_points_maison(score_maisons, i[réponse - 1], valeur * 2)
    print("Résumé des scores : ")
    for cle, valeur in score_maisons.items() :
        print(cle, ":", valeur, "points")
    return afficher_maison_gagnante(score_maisons)


questions = [
    (
        "Tu vois un ami en danger. Que fais-tu ?",
        ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    ),
    (
        "Quel trait te décrit le mieux ?",
        ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    ),
    (
        "Face à un défi difficile, tu...",
        ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    )
]