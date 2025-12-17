import json


def demander_texte(phrase):
    while True:
        reponse = input(phrase)
        if len(reponse) > 0:
            return reponse


def demander_nombre(phrase, minval=None, maxval=None):
    while True:
        saisie = input(phrase)
        est_bon_nombre = True
        for caractere in saisie:
            if caractere not in "0123456789":
                est_bon_nombre = False
                break
        if est_bon_nombre:
            nombre = 0
            for caractere in saisie:
                nombre = nombre * 10 + (ord(caractere) - ord('0'))


            if minval is None or nombre >= minval:
                if maxval is None or nombre <= maxval:
                    return nombre

        print("Erreur ! Entrez un nombre valide.")


def demander_choix(phrase, choices):
    print(phrase)
    print()
    for i in range(len(choices)):
        print(f"{i + 1}. {choices[i]}")
    print()
    reponse = int(demander_nombre("Votre choix : ", 1, len(choices)))
    return reponse


def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


