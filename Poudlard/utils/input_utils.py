import json


def demander_texte(phrase):
    if phrase == "":
        return "the phrase is empty"
    reponse = str(input(phrase ))
    while len(reponse) < 1:
        reponse = str(input(phrase ))
    return reponse

#Pas Pafait comme dans la consigne, à revoir
def demander_nombre(phrase, min_value = None, max_value = None):
    reponse = int(input(phrase ))
    if min_value is None:
        return reponse
    if max_value is None:
        return reponse
    else :
        while reponse < min_value or reponse > max_value:
            reponse = int(input(phrase))
    return reponse

def demander_choix(phrase, choices):
    print(phrase)
    print()
    for i in range (len(choices)):
        print(i +1, choices[i])
        print()
    reponse = int(input())
    while reponse <= 0 or reponse >= len(choices):
        reponse = int(input())
    return

def charger_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

