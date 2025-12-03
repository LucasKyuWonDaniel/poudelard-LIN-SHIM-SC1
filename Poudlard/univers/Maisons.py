def actualiser_points_maison(maisons, nom_maison, points) :
  if nom_maison in maisons :
    maisons[nom_maison] += points
    print (nom_maison, ":", maisons[nom_maison])
  else :
    return " la maison est introuvable"

def afficher_maison_gagnante(maisons) :
  max = maisons["Gryffondor"]
  for valeur in maisons.values() :
    if max < valeur :
      max = valeur
  for cle in maisons.keys() :
    if maisons[cle] == max :
      print(cle)

def repartition_maison(joueur, questions) :
  score_maisons = {
    "Gryffondor": 0, 
    "Serpentard": 0, 
    "Poufsouffle": 0, 
    "Serdaigle": 0 
  }


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
