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
