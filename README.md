Démarage

(venv) $ git clone https://framagit.org/jpython/share-code-plus.git
(venv) $ cd share-code-plus
(venv) $ pip install -r requirements.txt
(venv) $ set FLASK_ENV=development
(venv) $ python sharecode.py

Partie 1 : enregistrer le langage de programmation utilisé

-> python sharecode.py

Ajout d'un menu déroulant dans la page d'édition permettant de selectionner le code.
Ajout de l'extension correspondante dans le nom du fichier
Préselection du langage du code lors de l'édition d'un fichier


Partie 2 : Changez le procédé de stockage, plus de fichiers mais un SGBDR


-> python create_db.py
-> python sharecodedb.py

Création d'un nouveau model : model_sqlite.py
Réécriture de toutes les fonctions pour fonctionner avec sqlite

Réécriture reçues depuis sqlite


Partie 3 : enregistrez les infos sur les utilisateurs qui publient du code


-> python create_db.py
-> python sharecodedb.py


Nouvelle table users
Ajout d'une sauvegarde de l'adresse IP, du navigateur et de la date de modification
Ajout du template admin.html
Ajout d'un acces à la page admin de chaque code enregistré pour consulter les donnée d'enregistrementde ce code (IP, navigateur,date)
