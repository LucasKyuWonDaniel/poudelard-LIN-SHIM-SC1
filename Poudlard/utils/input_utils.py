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
        print("{}. {}".format(i + 1, choices[i]))
    print()
    reponse = int(demander_nombre("Votre choix : ", 1, len(choices)))
    return reponse

def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

































Maisons_data = {
  "Gryffondor": {
    "emoji": "🔥",
    "description": "Vous entrez dans une salle chaleureuse, décorée de rouge et d’or. Un feu crépite dans la cheminée, et des élèves rient autour des canapés.",
    "message_installation": "✨ Le courage et la loyauté sont à l'honneur ici. Bienvenue chez les lions !",
    "couleurs": ["rouge", "or"],
    "traits": ["courage", "bravoure", "loyauté"],
    "bonus_attributs": {
      "courage": 2,
      "loyauté": 1
    }
  },
  "Serpentard": {
    "emoji": "🐍",
    "description": "Vous découvrez une salle voûtée, éclairée par la lueur verte du lac. Les élèves vous observent avec curiosité et respect.",
    "message_installation": "✨ La ruse et l’ambition sont vos alliées. Bienvenue dans la noble maison Serpentard.",
    "couleurs": ["vert", "argent"],
    "traits": ["ruse", "ambition", "détermination"],
    "bonus_attributs": {
      "ambition": 2,
      "intelligence": 1
    }
  },
  "Poufsouffle": {
    "emoji": "🌻",
    "description": "Vous entrez dans une pièce confortable, aux murs recouverts de plantes et d’herbes magiques. L’atmosphère y est paisible et accueillante.",
    "message_installation": "✨ La patience et le travail sont vos plus grandes forces. Bienvenue à Poufsouffle !",
    "couleurs": ["jaune", "noir"],
    "traits": ["travail", "patience", "loyauté"],
    "bonus_attributs": {
      "loyauté": 2,
      "courage": 1
    }
  },
  "Serdaigle": {
    "emoji": "📘",
    "description": "Vous arrivez dans une salle lumineuse, pleine de livres et de cartes enchantées. Les discussions portent déjà sur la prochaine énigme du professeur Flitwick.",
    "message_installation": "✨ La sagesse et la curiosité t’accompagneront. Bienvenue chez les érudits de Serdaigle.",
    "couleurs": ["bleu", "bronze"],
    "traits": ["intelligence", "créativité", "curiosité"],
    "bonus_attributs": {
      "intelligence": 2,
      "ambition": 1
    }
  }
}

SORTS_DATA= [
    {
        "nom": "Lumos",
        "description": "Fait briller de la lumière à l'extrémité de la baguette.",
        "type": "Utilitaire"
    },
    {
        "nom": "Nox",
        "description": "Éteint la lumière produite par Lumos.",
        "type": "Utilitaire"
    },
    {
        "nom": "Alohomora",
        "description": "Déverrouille les portes et les objets fermés.",
        "type": "Utilitaire"
    },
    {
        "nom": "Wingardium Leviosa",
        "description": "Fait léviter des objets.",
        "type": "Utilitaire"
    },
    {
        "nom": "Lumos Solem",
        "description": "Produit une lumière très puissante simulant celle du soleil.",
        "type": "Utilitaire"
    },
    {
        "nom": "Aparecium",
        "description": "Rend visible l'encre invisible.",
        "type": "Utilitaire"
    },
    {
        "nom": "Obliviate",
        "description": "Efface des souvenirs spécifiques de la mémoire d'une personne.",
        "type": "Utilitaire"
    },
    {
        "nom": "Accio",
        "description": "Fait apparaître des objets vers le lanceur.",
        "type": "Utilitaire"
    },
    {
        "nom": "Reparo",
        "description": "Répare les objets cassés.",
        "type": "Utilitaire"
    },
    {
        "nom": "Expelliarmus",
        "description": "Désarme un adversaire.",
        "type": "Défensif"
    },
    {
        "nom": "Protego",
        "description": "Crée un bouclier magique pour bloquer les attaques.",
        "type": "Défensif"
    },
    {
        "nom": "Finite Incantatem",
        "description": "Met fin aux sorts ou effets en cours.",
        "type": "Défensif"
    },
    {
        "nom": "Petrificus Totalus",
        "description": "Pétrifie complètement la cible.",
        "type": "Offensif"
    },
    {
        "nom": "Stupefy",
        "description": "Assomme temporairement un adversaire.",
        "type": "Offensif"
    },
    {
        "nom": "Rictusempra",
        "description": "Fait rire de manière incontrôlable et affaiblit la cible.",
        "type": "Offensif"
    },
    {
        "nom": "Incendio",
        "description": "Crée une flamme.",
        "type": "Offensif"
    },
    {
        "nom": "Crucio",
        "description": "Inflige une douleur insupportable à la cible.",
        "type": "Offensif"
    },
    {
        "nom": "Imperio",
        "description": "Contrôle les actions de la cible.",
        "type": "Offensif"
    },
    {
        "nom": "Avada Kedavra",
        "description": "Provoque la mort instantanée de la cible.",
        "type": "Offensif"
    },
    {
        "nom": "Expecto Patronum",
        "description": "Convoque un Patronus pour repousser les Détraqueurs.",
        "type": "Défensif"
    },
    {
        "nom": "Diffindo",
        "description": "Coupe des objets avec précision.",
        "type": "Offensif"
    },
    {
        "nom": "Confringo",
        "description": "Provoque une explosion à l'impact.",
        "type": "Offensif"
    },
    {
        "nom": "Rennervate",
        "description": "Réanime une personne assommée ou inconsciente.",
        "type": "Défensif"
    },
    {
        "nom": "Incarcerous",
        "description": "Convoque des cordes pour ligoter la cible.",
        "type": "Offensif"
    }
]

QUIZ_DATA =[
  {"question": "Quel sort permet de désarmer un adversaire ? ", "reponse": "Expelliarmus"},
  {"question": "Quel sort est utilisé pour créer de la lumière ? ", "reponse": "Lumos"},
  {"question": "Quel sort éteint la lumière produite par Lumos ? ", "reponse": "Nox"},
  {"question": "Quel sort repousse un Détraqueur ? ", "reponse": "Expecto Patronum"},
  {"question": "Quel sort permet de faire léviter des objets ? ", "reponse": "Wingardium Leviosa"},
  {"question": "Quel est le sort de protection de base ? ", "reponse": "Protego"},
  {"question": "Quel sort permet d’ouvrir une porte verrouillée ? ", "reponse": "Alohomora"},
  {"question": "Quel sort permet de réparer des objets cassés ? ", "reponse": "Reparo"},
  {"question": "Quel sort permet de faire apparaître des objets ? ", "reponse": "Accio"},
  {"question": "Quel sort rend une cible muette ? ", "reponse": "Silencio"},
  {"question": "Quel sort fait apparaître une lumière rouge pour alerter ? ", "reponse": "Periculum"},
  {"question": "Quel sort crée du feu ? ", "reponse": "Incendio"},
  {"question": "Quel sort pétrifie complètement une cible ? ", "reponse": "Petrificus Totalus"},
  {"question": "Quel sort assomme temporairement un adversaire ? ", "reponse": "Stupefy"},
  {"question": "Quel sort fait rire de manière incontrôlable une cible ? ", "reponse": "Rictusempra"},
  {"question": "Quel sort efface des souvenirs précis d'une personne ? ", "reponse": "Obliviate"},
  {"question": "Quel sort révèle de l'encre invisible ? ", "reponse": "Aparecium"},
  {"question": "Quel sort produit une lumière intense simulant celle du soleil ? ", "reponse": "Lumos Solem"},
  {"question": "Quel sort permet de se léviter soi-même ? ", "reponse": "Wingardium Leviosa"},
  {"question": "Quel sort fait apparaître de l’eau ? ", "reponse": "Aguamenti"},
  {"question": "Quel sort fait apparaître un serpent ? ", "reponse": "Serpensortia"},
  {"question": "Quel sort provoque des étincelles ? ", "reponse": "Confringo"},
  {"question": "Quel sort crée un bouclier protecteur autour du lanceur ? ", "reponse": "Protego Maxima"},
  {"question": "Quel sort transforme un objet en autre chose ? ", "reponse": "Transfiguration"},
  {"question": "Quel sort peut rendre un objet invisible ? ", "reponse": "Sort de désillusion"},
  {"question": "Quel sort révèle des portes ou passages cachés ? ", "reponse": "Aparecium"},
  {"question": "Quel sort gèle instantanément l’eau ? ", "reponse": "Glacius"},
  {"question": "Quel sort ouvre une enveloppe magiquement scellée ? ", "reponse": "Alohomora"},
  {"question": "Quel sort fait flotter une personne sans défense ? ", "reponse": "Levicorpus"},
  {"question": "Quel sort crée une petite explosion ? ", "reponse": "Confringo"},
  {"question": "Quel sort produit un nuage de fumée ? ", "reponse": "Fumos"},
  {"question": "Quel sort permet de respirer sous l’eau ? ", "reponse": "Algue Gilly"},
  {"question": "Quel sort fait apparaître un Patronus ? ", "reponse": "Expecto Patronum"},
  {"question": "Quel sort peut transformer temporairement un objet en or ? ", "reponse": "Geminio"},
  {"question": "Quel sort repousse les créatures ? ", "reponse": "Repello Creatura"},
  {"question": "Quel sort répare le verre ou le métal cassé ? ", "reponse": "Reparo"},
  {"question": "Quel sort force quelqu’un à dire la vérité ? ", "reponse": "Veritaserum"},
  {"question": "Quel sort permet de léviter une personne ? ", "reponse": "Wingardium Leviosa"},
  {"question": "Quel sort permet de faire apparaître de la nourriture ? ", "reponse": "Sort de création de nourriture"},
  {"question": "Quel sort supprime les maléfices ou les jinxes ? ", "reponse": "Finite Incantatem"},
  {"question": "Quel sort nettoie des objets magiquement ? ", "reponse": "Scourgify"},
  {"question": "Quel sort endort une personne ? ", "reponse": "Sort Somnus"},
  {"question": "Quel sort coupe des liens ou des cordes ? ", "reponse": "Diffindo"},
  {"question": "Quel sort fait apparaître un balai ? ", "reponse": "Charme d’invocation / Accio Balai"},
  {"question": "Quel sort crée une cage protectrice autour d’une personne ? ", "reponse": "Cave Inimicum"},
  {"question": "Quel sort rend quelqu’un invisible temporairement ? ", "reponse": "Sort de désillusion"},
  {"question": "Quel sort crée une corde ou un lasso magique ? ", "reponse": "Incarcerous"},
  {"question": "Quel sort peut désactiver temporairement une baguette ? ", "reponse": "Expulso"},
  {"question": "Quel sort illumine de l’eau sombre ? ", "reponse": "Lumos Solem"},
  {"question": "Quel sort produit des étincelles pour enflammer quelque chose ? ", "reponse": "Incendio"},
  {"question": "Quel sort bannit des créatures ou objets maléfiques ? ", "reponse": "Finite Incantatem"}
]

Data_quidditch ={
  "Gryffondor": {
    "capitaine": "Harry Potter",
    "joueurs": [
      "Harry Potter (Attrapeur)",
      "Ginny Weasley (Chasseuse)",
      "Katie Bell (Chasseuse)",
      "Demelza Robins (Chasseuse)",
      "Ron Weasley (Gardien)",
      "Jimmy Peakes (Batteur)",
      "Ritchie Coote (Batteur)"
    ]
  },
  "Serpentard": {
    "capitaine": "Drago Malefoy",
    "joueurs": [
      "Drago Malefoy (Attrapeur)",
      "Cassius Warrington (Chasseur)",
      "Graham Montague (Chasseur)",
      "Urquhart (Chasseur)",
      "Miles Bletchley (Gardien)",
      "Vincent Crabbe (Batteur)",
      "Gregory Goyle (Batteur)"
    ]
  },
  "Serdaigle": {
    "capitaine": "Cho Chang",
    "joueurs": [
      "Cho Chang (Attrapeuse)",
      "Roger Davies (Chasseur)",
      "Michael Corner (Chasseur)",
      "Jeremy Stretton (Chasseur)",
      "Grant Page (Gardien)",
      "Jason Samuels (Batteur)",
      "Randall Phelps (Batteur)"
    ]
  },
  "Poufsouffle": {
    "capitaine": "Cedric Diggory",
    "joueurs": [
      "Cedric Diggory (Attrapeur)",
      "Heidi Macavoy (Chasseuse)",
      "Zacharias Smith (Chasseur)",
      "Jason Samuels (Chasseur)",
      "Herbert Fleet (Gardien)",
      "Anthony Rickett (Batteur)",
      "Maxine O'Flaherty (Batteuse)"
    ]
  }
}
