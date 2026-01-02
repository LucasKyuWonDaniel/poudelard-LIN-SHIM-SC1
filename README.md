poudelard-LIN-SHIM-SC1

Jeu d'aventure interactif inspiré de Harry Potter, implémenté en Python avec gestion de chapitres narratifs, 
maisons de Poudlard, sorts, quiz et match de Quidditch. Projet réalisé en binôme pour le module TI101 à l'EFREI.

Contributeurs: SHIM Daniel et LIN Lucas

Installation :
Clonez le dépôt GitHub :
                                A copier dans votre IDE 
git clone https://github.com/LucasKyuWonDaniel/poudelard-LIN-SHIM-SC1.git
cd poudelard-LIN-SHIM-SC1

Utilisation :
Exécutez le jeu via :    python main.py
Le menu principal s'affiche pour lancer les chapitres successivement ou quitter. 
Utilisez les touches numériques pour les choix et validez avec Entrée. 
Les saisies sont validées automatiquement via input_utils.py.

Fonctionnalités :
  - Création de personnage avec nom, prénom, attributs (courage, intelligence, loyauté, ambition) et gestion d'inventaire/argent.
​
  - Quatre chapitres narratifs : arrivée à Poudlard (Chapitre 1), 
répartition maison (Chapitre 2), apprentissage sorts/quiz (Chapitre 3), match Quidditch (Chapitre 4).
​
  - Répartition maison via quiz interactif et actualisation points maisons.​

  - Mini-jeux : achats Chemin de Traverse, quiz magie, simulation Quidditch avec équipes et Vif d'Or.​

  - Sauvegarde/chargement via JSON et affichage profil joueur/maisons.

Répartition des Tâches :
  - Daniel SHIM : input_utils.py, univers/personnage.py, chapitres/chapitre1.py, chapitres/chapitre4.py, menu.py
​
  - Lucas LIN : univers/maison.py, chapitres/chapitre2.py, chapitres/chapitre3.py, , main.py
