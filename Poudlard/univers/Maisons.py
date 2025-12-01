def actualiser_points_maison(maisons, nom_maison, points) :
  if nom_maison in maisons :
    maisons[nom_maison] += points
    print (nom_maison, ":", maisons[nom_maison])
  else :
    return " la maison est introuvable"
