# Application de gestion de stock - Pharmacie

Application console en Python avec une connexion à une base de données MySQL permettant la gestion  
de stock des produits avec 7 modules principaux : 

- employe
- fournisseur
- produit
- entree 
- sortie 
- ligne_entree
- ligne_sortie

## Fonctionnalités principales 
### Gestion des employés :
- Ajouter un employé
- Modifier un employé
- Rechercher un employé
- Consulter un employé
- lister les employés 
- Désactiver/ Activer un employé


### Gestion des fournisseurs
- Ajouter un fournisseur 
- Modifier un fournisseur
- Rechercher un fournisseur
- Consulter un fournisseur
- lister les fournisseurs
- Désactiver/ Activer un fournisseur

### Gestion des produits
- Ajouter un produit
- Modifier un produit
- Rechercher un produit
- Consulter un produit
- lister les produits
- Désactiver/ Activer un produit
- Vérifier l'état du stock d'un produit

### Gestion des entrees
- Ajouter une entree
- Modifier une entree
- Consulter une entree
- Rechercher une entree 
- lister toutes les entrees 


### Gestion des sorties
- Ajouter  une sortie
- Modifier une sortie
- Consulter une sortie
- Rechercher une  sortie
- lister toutes les sorties

## Gestion des lignes entree
- Ajouter une ligne entree
- Modifier une ligne entree
- Lister toutes les lignes entree

## Gestion des lignes sortie
- Ajouter une ligne sortie
- Modifier une ligne sortie
- Lister toutes les lignes sortie


## Technologies utilisées

- Python 3.13.6 langage de principale
- Mysql 9.3.0 for Win64 base de données relationnelles
- Mysql-connector-python / connexion python à Mysql
- Prettytable tables de données

## prérequis

- Python 3.10 ou supérieur
- Mysql 5.7 ou supérieur
- Driver mysql-connector-python 

## Installation

## configuration de la base de données

1 démarrer le terminal
2 création de la base de données : 

preciser le chemin du dossier du repertoire dans lequel est contenu le fichier create_database.Sql
puis lancer la creation de la base de données avec la commande suivante :

PS C:\Users\@nameusers > mysql -u root -p < database\create_database.sql

resultat attendu :

base de données gestion_stock créee avec succès !
nombre de lignes contenu dans chaque table : ***

3 vérification de la création de la base de données 

- mysql -u root -p;
- Show databases;
- use gestion_stock
- show tables;

## configuration de l'application de gestion du stock python

1 télécharger le driver mysql-connector-python-9.5.0 
2 lancer l'invite de commande 
3 installer la driver pour la version python installée sur votre ordinateur :

- si  pip est dans le PATH  : pip install mysql-connector-python

- sinon lancer pip via python : PS C:\Users\@nameuser > cd &"C:\Users\@nameuser\AppData\Local\Programs\Python\Python313\python.exe" -m pip install mysql-connector-python

4 configuration de la connexion de python à mysql dans le programme :

- Modifier les paramètres de connexion dans le fichier config.py contenu dans le dossier Configuration
- path : > Cd Projet-tutoré-python\Configuration
config.py :

#importation du module mysql.connector pour connecter python 

import mysql.connector

#definition la fonction get_connection() 
#modifier ces informations de connexion en fonction des vôtres

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=" votre mot de passe",
        database="gestion_stock",
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci"
    )

## exécution sur vscode

1 Dans votre éditeur de texte Dirigez vous dans le dossier src\main.py 
2 lancer un terminal depuis l'espace de travail courant : CTRL + Shift + p
3 exécution du programme : python -m src.main

## struture du travail 

C:.
│   Readme.md
│
├───Configuration
│      config.py
│      __init__.py
│   
│   
│
├───crud
│      crud_employe.py
│      crud_entree.py
│      crud_fournisseur.py
│      crud_ligne_entree.py
│      crud_ligne_sortie.py
│      crud_produit.py
│      crud_sortie.py
│      __init__.py
│  
│   
│
├───database
│       create_database.sql
│       drop_database.sql
│       reset_database.sql
│
├───modules
│      employe.py
│      entree.py
│      fournisseur.py
│      ligne_entree.py
│      ligne_sortie.py
│      produit.py
│      sortie.py
│      __init__.py
│   
│   
│
├───src
│      main.py
│      __init__.py
│   
│  
│
└───utils
       utils.py
       __init__.py
    
    

## structure de la base de données 

## Table fournisseurs

id_fournisseurs : Identifiant unique (AUTO_INCREMENT)
matricule : Matricule du fournisseur (unique)
nom : Nom du fournisseur
adresse : Adresse complète
mobile : Numéro de téléphone
email : Adresse email
statut : État (1=actif, 0=inactif)

## Table employes

id_employes : Identifiant unique (AUTO_INCREMENT)
matricule : Matricule de l’employé (unique)
nom : Nom
prenom : Prénom
date_naissance : Date de naissance
genre : Sexe (M/F)
adresse : Adresse complète
mobile : Téléphone
email : Email
fonction : Rôle dans la pharmacie
date_creation : Date d’enregistrement
statut : État (1=actif, 0=inactif)

## Table produits

id_produits : Identifiant unique
id_fournisseurs : Référence fournisseur (FK)
ref_produit : Référence interne (unique)
code_atc : Code ATC du médicament
nom_commercial : Nom commercial
dci : Dénomination commune internationale
dosage : Dosage
forme : Forme pharmaceutique
conditionnement : Conditionnement
stock_minimum : Stock minimum
stock_maximum : Stock maximum
description_produit : Description
statut : État (1=actif, 0=inactif)

## Table gestion_entree

id_entrees : Identifiant unique
id_fournisseurs : Référence fournisseur (FK)
date_commande : Date de la commande
statut_commande : Statut (en cours / validée / annulée)
date_reception : Date de réception
observation : Notes éventuelles

## Table ligne_entree

id_ligne : Identifiant unique
id_entrees : Référence de l’entrée (FK)
id_produits : Produit concerné (FK)
numero_lot : Numéro de lot
peremption : Date de péremption
quantite : Quantité reçue
prix_unitaire_entree : Prix d’achat unitaire
emplacement : Zone de stockage (Z-PMO, Z-TAC, Z-Q, Z-ER.)

## Table gestion_sortie

id_sorties : Identifiant unique
id_employes : Employé responsable (FK)
date_sortie : Date de la sortie
destinataire : Particulier / Professionnel
statut : Libre accès / Sous ordonnance
observation : Notes éventuelles

## Table ligne_sortie

id_ligne : Identifiant unique
id_sorties : Référence sortie (FK)
id_produits : Produit concerné (FK)
numero_lot : Numéro de lot
peremption : Date de péremption
quantite : Quantité sortie
prix_unitaire_vente : Prix de vente unitaire


##  Contribution

Pour contribuer au projet :
1. Fork le repository
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

##  Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.








