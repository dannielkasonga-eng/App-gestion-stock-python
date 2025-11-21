from Configuration.config import get_connection
from utils.utils import demande_champ
from utils.utils import demander_matricule_existant_e
from utils.utils import demander_matricule_existant_f
from utils.utils import demander_ref_produit_existant
from utils.utils import demander_identifiants_entree_existante
from utils.utils import demander_identifiants_sortie_existante

#Importation du module employe et fonctions crud employe

from crud.crud_employe import (
    ajouter_employe,
    modifier_employe,
    consulter_employe,
    rechercher_employe,
    lister_employes,
    desactiver_employe,
    activer_employe,
 )
from modules.employe import Employe 

#importation du module fournisseur et fonctions crud fournisseurs

from crud.crud_fournisseur import (
    ajouter_fournisseur,
    modifier_fournisseur,
    consulter_fournisseur,
    rechercher_fournisseur,
    lister_fournisseurs,
    desactiver_fournisseur,
    activer_fournisseur,  
)
from modules.fournisseur import Fournisseur

#importation du module produit et fonctions crud produit

from crud.crud_produit import (
    ajouter_produit,
    modifier_produit,
    consulter_produit,
    rechercher_produit,
    lister_produits,
    desactiver_produit,
    activer_produit,
    id_produits_existe
)
from modules.produit import Produit


#importation du module entree et fonctions crud entree

from crud.crud_entree import (
    ajouter_entree,
    modifier_entree,
    consulter_entree,
    lister_entree,
    entree_existe
)
from modules.entree import Entree

#importation du module sortie et fonctions crud sortie

from crud.crud_sortie import (
    ajouter_sortie,
    modifier_sortie,
    consulter_sortie,
    lister_sortie,
    employe_peut_sortir,
    sortie_existe
)
from modules.sortie import Sortie

#creation menu module employe

def menu_employe():
    while True :
        print("""
---GESTION DES EMPLOYES---
1. Ajouter un employé
2. Modifier un employé
3. Rechercher un employé
4. Consulter un employé
5. Lister les employés
6. Désactiver un employé
7. Activer un employé
8. Retourner au menu principal
0. Quitter le programme             
""")
        
        choix = input("choisissez une option :")

        if choix == "1":
            print("\n--- AJOUT D'UN NOUVEL EMPLOYÉ ---")

            emp = Employe(
                matricule=demande_champ("Matricule"),
                nom=demande_champ("Nom"),
                prenom=demande_champ("Prénom"),
                date_naissance=demande_champ("Date de naissance"),
                genre=demande_champ("Genre"),
                adresse=demande_champ("Adresse"),
                mobile=demande_champ("Mobile"),
                email=demande_champ("Email"),
                fonction=demande_champ("Fonction")
            )

            ajouter_employe(emp)
            print("\nEmployé ajouté avec succès.\n")

        elif choix == "2":
            print("\n--- MODIFICATION D'UN EMPLOYÉ ---")
            matricule = demander_matricule_existant_e("Matricule de l'employé à modifier")
            if matricule is None:
                continue

            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            emp = Employe(
                nom=input("Nom : ") or None,
                prenom=input("Prénom : ") or None,
                date_naissance=input("Date de naissance : ") or None,
                genre=input("Genre : ") or None,
                adresse=input("Adresse : ") or None,
                mobile=input("Mobile : ") or None,
                email=input("Email : ") or None,
                fonction=input("Fonction : ") or None,
                statut="1"
            )

            modifier_employe(matricule, emp)
            print("\nEmployé modifié avec succès.\n")

        elif choix == "3":
            print("\n--- RECHERCHE D'EMPLOYÉS ---")
            print('Note : pour plusieurs matricules, séparez par ","')
            chaine = demande_champ("Entrez les matricules")
            liste = [m.strip() for m in chaine.split(",")]

            table = rechercher_employe(liste)
            print("\n" + table.get_string() + "\n")

        elif choix == "4":
            print("\n--- CONSULTATION EMPLOYÉ(S) ---")
            print('Note : pour plusieurs matricules, séparez par ","')
            chaine = demande_champ("Entrez les matricules")
            table = consulter_employe(chaine)

            print("\n" + table.get_string() + "\n")

        elif choix == "5":
            print("\n--- LISTE DES EMPLOYÉS ---")
            table = lister_employes()
            print("\n" + table.get_string() + "\n")

        elif choix == "6":
            print("\n--- DÉSACTIVER UN EMPLOYÉ ---")
            matricule = demander_matricule_existant_e("Matricule à désactiver")
            if matricule:
                desactiver_employe(matricule)
                print("\nEmployé désactivé.\n")

        elif choix == "7":
            print("\n--- ACTIVER UN EMPLOYÉ ---")
            matricule = demander_matricule_existant_e("Matricule à activer")
            if matricule:
                activer_employe(matricule)
                print("\nEmployé activé.\n")

        elif choix =="8":
            menu_principal()
        elif choix=="0":
            print("Bye...")
            break
        else:
            print("Option invalide, réessayer.\n")


#creation menu module fournisseur

def menu_fournisseur():
    while True:
        print("""
---GESTION DES FOURNISSEURS---
1. Ajouter un fournisseur
2. Modifier un fournisseur
3. Rechercher un fournisseur
4. Consulter un fournisseur
5. Lister les fournisseurs
6. Désactiver un fournisseurs
7. Activer un fournisseurs
8. Retourner au menu principal
0. Quitter le programme             
""")
        choix = input("choisissez une option").strip()
        if choix == "1":
            print("\n--- AJOUT D'UN NOUVEAU FOURNISSEUR ---")
            fournisseur = Fournisseur(
                matricule=demande_champ("Matricule"),
                nom=demande_champ("Nom"),
                adresse=demande_champ("Adresse"),
                mobile=demande_champ("Mobile"),
                email=demande_champ("Email")
            )
            ajouter_fournisseur(fournisseur)
            print("\nFournisseur ajouté avec succès.\n")

        elif choix == "2":
            print("\n--- MODIFICATION D'UN FOURNISSEUR ---")
            matricule = demander_matricule_existant_f("Matricule du fournisseur à modifier")
            if matricule is None:
                continue

            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            fournisseur = Fournisseur(
                nom=input("Nom : ") or None,
                adresse=input("Adresse : ") or None,
                mobile=input("Mobile : ") or None,
                email=input("Email : ") or None,
                statut=input("Statut (1=actif, 0=inactif) : ") or "1"
            )
            modifier_fournisseur(matricule, fournisseur)
            print("\nFournisseur modifié avec succès.\n")

        elif choix == "3":
            print("\n--- RECHERCHE DE FOURNISSEUR(S) ---")
            print('Note : pour plusieurs matricules, séparez par ","')
            chaine = demander_matricule_existant_f("Entrez les matricules à rechercher")
            table = rechercher_fournisseur(chaine)
            print("\n" + table.get_string() + "\n")

        elif choix == "4":
            print("\n--- CONSULTATION DÉTAILLÉE DE FOURNISSEUR(S) ---")
            print('Note : pour plusieurs matricules, séparez par ","')
            chaine = demander_matricule_existant_f("Entrez les matricules à consulter")
            table = consulter_fournisseur(chaine)
            print("\n" + table.get_string() + "\n")

        elif choix == "5":
            print("\n--- LISTE DES FOURNISSEURS ---")
            table = lister_fournisseurs()
            print("\n" + table.get_string() + "\n")

        elif choix == "6":
            print("\n--- DÉSACTIVER UN FOURNISSEUR ---")
            matricule = demander_matricule_existant_f("Matricule à désactiver")
            if matricule:
                desactiver_fournisseur(matricule)
                print("\nFournisseur désactivé avec succès.\n")

        elif choix == "7":
            print("\n--- ACTIVER UN FOURNISSEUR ---")
            matricule = demander_matricule_existant_f("Matricule à activer")
            if matricule:
                activer_fournisseur(matricule)
                print("\nFournisseur activé avec succès.\n")
        elif choix =="8":
            menu_principal()
        elif choix=="0":
            print("Bye...")
            break
        else:
            print("Option invalide, réessayez.\n")

#creation menu module produit

def menu_produit():
    while True:
        print("""
---GESTION DES PRODUITS---
1. Ajouter un produit
2. Modifier un produit
3. Rechercher un produit
4. Consulter un produit
5. Lister les produits
6. Désactiver un produit
7. Activer un produit
8. Vérifier l'état du stock des produits          
9. Retourner au menu principal
0. Quitter le programme             
""")
        choix = input("Choisissez une option :")
        
        if choix == "1":
            print("\n--- AJOUT D'UN NOUVEAU PRODUIT ---")

            prod = Produit(
                ref_produit=demande_champ("Référence produit"),
                code_atc=demande_champ("Code ATC"),
                nom_commercial=demande_champ("Nom commercial"),
                dci=demande_champ("DCI"),
                description=demande_champ("Description"),
                stock_minimum=demande_champ("Stock minimum"),
                stock_maximum=demande_champ("Stock maximum")
            )

            ajouter_produit(prod)
            print("\nProduit ajouté avec succès.\n")

        elif choix == "2":
            print("\n--- MODIFICATION D'UN PRODUIT ---")
            ref_prod = demander_ref_produit_existant("Référence du produit à modifier")
            if ref_prod is None:
                continue

            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            prod = Produit(
                code_atc=input("Code ATC : ") or None,
                nom_commercial=input("Nom commercial : ") or None,
                dci=input("DCI : ") or None,
                description=input("Description : ") or None,
                stock_minimum=input("Stock minimum : ") or None,
                stock_maximum=input("Stock maximum : ") or None,
                statut="1"
            )

            modifier_produit(ref_prod, prod)
            print("\nProduit modifié avec succès.\n")

        elif choix == "3":
            print("\n--- RECHERCHE DE PRODUIT ---")
            ref = demander_ref_produit_existant("Entrez la référence du produit")
            if not ref:
                break
            table = rechercher_produit(ref)
            print("\n" + table.get_string() + "\n")


        elif choix == "4":
            print("\n--- CONSULTATION D'UN PRODUIT ---")
            ref = demander_ref_produit_existant("Entrez la référence du produit")
            if not ref:
                break
            table = consulter_produit(ref)
            print("\n" + table.get_string() + "\n")


        elif choix == "5":
            print("\n--- LISTE DES PRODUITS ---")
            table = lister_produits()
            print("\n" + table.get_string() + "\n")

        elif choix == "6":
            print("\n--- DÉSACTIVER UN PRODUIT ---")
            ref_prod = demander_ref_produit_existant("Référence à désactiver")
            if ref_prod:
                desactiver_produit(ref_prod)
                print("\nProduit désactivé.\n")

        elif choix == "7":
            print("\n--- ACTIVER UN PRODUIT ---")
            ref_prod = demander_ref_produit_existant("Référence à activer")
            if ref_prod:
                activer_produit(ref_prod)
                print("\nProduit activé.\n")

        elif choix == "8":
            print("\n--- VÉRIFICATION DE L'ÉTAT DU STOCK ---")
            tentatives = 0

            while True:
                ref = input("Entrez l'identifiant numérique du produit (id_produits) : ").strip()
                # 1. Vérification : entier ?
                if not ref.isdigit():
                    print("\n\033[1;31mErreur : L'identifiant du produit doit être un nombre entier.\033[0m")
                    tentatives += 1
                else:
                    ref = int(ref)

                    # 2. Vérification existence en base
                    if id_produits_existe(ref):
                        break
                    else:
                        print("\nRéférence erronée ou non sauvegardée.")
                        tentatives += 1
                        
                if tentatives >= 3:
                    print("\nVous avez oublié la référence ?")
                    print("Conseil : consultez la liste des produits.\n")
                    return menu_principal()

            # Produit valide → affichage du stock
            produit = Produit(id_produits=ref)
            resultat = produit.etat_stock()
            print("\nÉtat du stock pour le produit ID :", ref)
            print(resultat)

        elif choix =="9":
            menu_principal()
            break
        else:
            print("Option invalide. Réessayer.")


#creation menu module entree

def menu_entree():
    while True:
        print("""
---GESTION DES ENTREES---
1. Ajouter une entree
2. Modifier une entree
3. Consulter une entree
4. Lister les entrees
5. Retourner au menu principal
0. Quitter le programme             
""")
        choix = input("Choisissez une option :")
        if choix == "1":
            print("\n--- AJOUT D'UNE NOUVELLE ENTREE ---")

            # Vérification ID fournisseur
            tentatives = 0
            id_f = None

            while tentatives < 3:
                id_f = input("Identifiant du fournisseur : ").strip()

                if rechercher_fournisseur(id_f):      
                    break
                else:
                    print("\033[31mErreur !\033[0m id erronné ou non sauvegardé. Réessayez :")
                    tentatives += 1

            if tentatives == 3:
                print("Avez-vous oublié l'identifiant ?")
                print("Conseil : consultez la liste des fournisseurs")
                continue

            # Champs restants
            statut = demande_champ("Statut")
            observation = demande_champ("Observation")
            entree = Entree(
                id_fournisseurs=id_f,
                statut_commande=statut,
                observation=observation
            )

            ajouter_entree(entree)
            print("Entrée sauvegardée avec succès !")

        elif choix == "2":
            print("\n--- MODIFICATION D'UNE ENTREE ---")

            # Récupération validée de l'identifiant entrée + fournisseur
            identifiants = demander_identifiants_entree_existante(
                "ID de l'entrée", 
                "ID du fournisseur"
            )
            if identifiants is None:
               continue

            id_entrees, id_fournisseurs = identifiants

            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            # Saisie des nouveaux champs (None = ne pas modifier)
            entree = Entree(
                id_fournisseurs=input("ID fournisseur :").strip() or None,
                statut_commande=input("Statut commande : ").strip() or None,
                observation=input("Observation : ").strip() or None
            )

            # Construction du dictionnaire comme exige le CRUD
            nouveaux_champs = {}

            if entree.id_fournisseurs is not None:
                nouveaux_champs["id_fournisseur"] = entree.id_fournisseurs
            if entree.statut_commande is not None:
                nouveaux_champs["statut_commande"] = entree.statut_commande
            if entree.observation is not None:
                nouveaux_champs["observation"] = entree.observation
            if not nouveaux_champs:
                print("Aucune modification effectuée.")
                continue

            modifier_entree(id_entrees, id_fournisseurs, nouveaux_champs)
            print("\nEntrée modifiée avec succès.\n")

        elif choix == "3":
            print("\n--- CONSULTER UNE ENTREE ---")

            id_e = input("ID de l'entrée : ").strip()
            id_f = input("ID du fournisseur : ").strip()

            if not entree_existe(id_e, id_f):
                print("\033[31mEntrée non sauvegardée\033[0m")
                print("\033[31mConseil : Consultez la liste des entrées\033[0m")
                continue

            table = consulter_entree(id_e, id_f)
            print(f"Voici les informations trouvées pour {id_e} et {id_f}")
            print(table)

        elif choix == "4":
            print("\n--- LISTE DES ENTREES ---")
            print(lister_entree())

        elif choix =="5":
            menu_principal()
        elif choix=="0":
            print("Bye...")
            break
        else:
            print("Option invalide. Réessayer.")

#creation menu module sortie

def menu_sortie():
    while True:
        print("""
---GESTION DES SORTIES---
1. Ajouter une sortie
2. Modifier une sortie
3. Consulter une sortie
4. Lister les sorties
5. Retourner au menu principal
0. Quitter le programme             
""")
        choix = input("Choisissez une option :")
        if choix == "1":
            print("\n--- AJOUT D'UNE NOUVELLE SORTIE ---")
            print("Note : seuls le pharmacien adjoint, assistant et caissier peuvent effectuer une sortie.\n")
            
            #vérification ID employe
            tentatives = 0
            id_e = None

            while tentatives < 3:
                id_e = input("Identifiant de l'employé : ").strip()

                if employe_peut_sortir(id_e):
                    break
                else:
                    print("\033[31mErreur !\033[0m id erronné ou non sauvegardé. Réessayez :")
                    tentatives += 1

            if tentatives == 3:
                print("Avez-vous oublié l'identifiant ?")
                print("Conseil : consultez la liste des employés")
                continue

            destinataire = demande_champ("Destinataire (particulier/professionnel)")
            statut = demande_champ("Statut")
            observation = demande_champ("Observation (libre d'accès / sous ordonnance)")
            #champ_restants
            sortie = Sortie(
                id_employes=id_e,
                destinataire=destinataire,
                statut=statut,
                observation=observation
            )

            ajouter_sortie(sortie)
            print("Sortie sauvegardée avec succès !")

        elif choix == "2":
            print("\n--- MODIFICATION D'UNE SORTIE ---")

            # Récupération validée de l'identifiant sortie + employe
            identifiants = demander_identifiants_sortie_existante(
                "ID de la sortie", 
                "ID de l'employe"
            )

            if identifiants is None:
                continue
            id_sorties, id_employes = identifiants

            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            # Saisie des nouveaux champs (None = ne pas modifier)
            sortie = Sortie(
                id_employes=input("ID employes :").strip() or None,
                statut =input("Statut sortie : ").strip() or None,
                observation=input("Observation : ").strip() or None
            )

            # Construction du dictionnaire comme exige le CRUD
            nouveaux_champs = {}

            if sortie.id_employes is not None:
                nouveaux_champs["id_employes"] = sortie.id_employes
            if sortie.statut is not None:
                nouveaux_champs["statut_sortie"] = sortie.statut
            if sortie.observation is not None:
                nouveaux_champs["observation"] = sortie.observation
            if not nouveaux_champs:
                print("Aucune modification effectuée.")
                continue

            modifier_sortie(id_sorties, id_employes, nouveaux_champs)
            print("\nEntrée modifiée avec succès.\n")    

        elif choix == "3":
            print("\n--- CONSULTER UNE SORTIE ---")

            id_s = input("ID de la sortie : ").strip()
            id_e = input("ID de l'employé : ").strip()

            if not sortie_existe(id_s, id_e):
                print("\033[31mSortie non sauvegardée\033[0m")
                print("\033[31mConseil : Consultez la liste des sorties\033[0m")
                continue

            table = consulter_sortie(id_s, id_e)
            print(f"Voici les informations trouvées pour {id_s} et {id_e}")
            print(table)

        elif choix == "4":
            print("\n--- LISTE DES SORTIES ---")
            print(lister_sortie())

        elif choix =="5":
            menu_principal()
        elif choix=="0":
            print("Bye...")
            break
        else:
            print("Option invalide. réessayez.")

#creation menu module ligne_entree

def menu_ligne_entree():
    while True:
        print("""
---GESTION DES LIGNES ENTREE---
1. Ajouter une ligne entree
2. Modifier une ligne entree
3. Lister les lignes entree
4. Retourner au menu principal
0. Quitter le programme             
""")
        choix = input("Choisissez une option :")
        if choix =="1":
            print("bonjour")
        elif choix =="4":
            menu_principal()
        elif choix=="0":
            print("Bye...")
            break
        else:
            print("Option invalide. Réessayez.")

#creation menu module ligne_sortie

def menu_ligne_sortie():
    while True:
        print("""
---GESTION DES LIGNES SORTIE---
1. Ajouter une ligne sortie
2. Modifier une ligne sortie
3. Lister les lignes sortie
4. Retourner au menu principal
0. Quitter le programme             
""")
        choix = input("Choisissez une option :")
        if choix =="1":
            print("bonjour")
        elif choix =="4":
            menu_principal()
        elif choix=="0":
            print("Bye...")
            break
        else:
            print("Option invalide. Réessayez.")

#creation menu principal

def menu_principal():
    while True:
        print("""
---MENU PRINCIPAL---
1. Gestion des employés
2. Gestion des fournisseurs
3. Gestion des produits              
4. Gestion des entrees
5. Gestion des sorties
6. Gestion des lignes entree
7. Gestion des lignes sortie
0. Quitter le programme             
""")
        choix = input("Choisissez une option :")

        if choix == "1":
            menu_employe()

        elif choix == "2":
            menu_fournisseur()

        elif choix == "3":
            menu_produit()
        
        elif choix == "4":
            menu_entree()

        elif choix == "5":
            menu_sortie()

        elif choix == "6":
            menu_ligne_entree()

        elif choix == "7":
            menu_ligne_sortie()

        elif choix == "8":
            print("Bye....")
            break
        else:
            print("Option invalide. Réessayez.")
        
def tester_connexion_db():
    """Vérifie si la connexion MySQL fonctionne correctement."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")  # simple requête test
        cursor.fetchone() #vide le resultat avant de fermer le curseur
        cursor.close()
        conn.close()
        print("La connexion à la base de données est établie avec succès !")
        return True
    except Exception as e:
        print("Erreur : impossible de se connecter à la base de données !")
        print("Vérifiez que le module de connexion python à mysql est bien installé")
        print("et que la base de données 'gestion_stock' existe.")
        print(f"Détails de l'erreur : {e}")
        return False

def application_gestion_stock():
    print("--- APPLICATION DE GESTION STOCK ---")

    if not tester_connexion_db():
        print("Arrêt de l'application.")
        return  # On ne démarre pas les menus sans connexion valide

    print("Initialisation de l'application en cours")
    print("Chargement du menu principal...")
    menu_principal()

# Point d'entrée du programme
if __name__== "__main__":
    application_gestion_stock()



