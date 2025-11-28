from Configuration.config import get_connection
from utils.utils import demande_champ
from utils.utils import demander_matricule_existant_e
from utils.utils import demander_matricule_existant_f
from utils.utils import demander_ref_produit_existant
from utils.utils import demander_identifiants_entree_existante
from utils.utils import demander_identifiants_sortie_existante
from utils.utils import demander_identifiants_ligne_entree_existante
from utils.utils import demander_identifiants_ligne_sortie_existante


#Importation du module employe et fonctions crud employe

from crud.crud_employe import (
    ajouter_employe,
    modifier_employe,
    consulter_employe,
    rechercher_employe,
    lister_employes,
    desactiver_employe,
    activer_employe,
    get_employe_by_matricule

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
    get_fournisseur_by_matricule  
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
    id_produits_existe,
    get_produit_by_ref_produit
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

#Importation du module ligne_entree et fonctions crud ligne_entree

from crud.crud_ligne_entree import (
    ajouter_ligne_entree,
    modifier_ligne_entree,
    lister_ligne_entree
)
from crud.crud_entree import rechercher_entree
from crud.crud_produit import rechercher_produit
from modules.ligne_entree import LigneEntree

from crud.crud_ligne_sortie import (
    ajouter_ligne_sortie,
    modifier_ligne_sortie,
    lister_ligne_sortie
)
from crud.crud_sortie import rechercher_sortie
from crud.crud_produit import rechercher_produit
from modules.ligne_sortie import LigneSortie

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
            
            #Récupérer l'employé existant
            employe_actuel = get_employe_by_matricule(matricule)
            if not employe_actuel:
                print("\033[31mEmploye introuvable.\033[0m\n")
                continue
            
            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")
           
            # IMPORTANT : remplacer vide == conserver
            matricule = input(f"Matricule [{employe_actuel['matricule']}]: ").strip()
            if matricule == "":
                matricule = employe_actuel["matricule"] #conserve le matricule actuel


            nom = input(f"Nom [{employe_actuel['nom']}]: ").strip()
            if nom == "":
                nom = employe_actuel["nom"]

            prenom = input(f"Prenom [{employe_actuel['prenom']}]: ").strip()
            if prenom == "":
                prenom = employe_actuel["prenom"]

            date_naissance = input(f"Date de naissance [{employe_actuel['date_naissance']}]: ").strip()
            if date_naissance == "":
                date_naissance = employe_actuel["date_naissance"]

            genre = input(f"Genre [{employe_actuel['genre']}]: ").strip()
            if genre == "":
                genre = employe_actuel["genre"]

            adresse = input(f"Adresse [{employe_actuel['adresse']}]: ").strip()
            if adresse == "":
                adresse = employe_actuel["adresse"]

            mobile = input(f"Mobile [{employe_actuel['mobile']}]: ").strip()
            if mobile == "":
                mobile = employe_actuel["mobile"]

            email = input(f"Email [{employe_actuel['email']}]: ").strip()
            if email == "":
                email = employe_actuel["email"]

            fonction = input(f"Fonction [{employe_actuel['fonction']}]: ").strip()
            if fonction == "":
                fonction = employe_actuel["fonction"]

            statut = input(f"Statut (1=actif,0=inactif) [{employe_actuel['statut']}]: ").strip()
            if statut not in ("0", "1"):
                statut = employe_actuel["statut"]
                
            else:
                statut = statut 
                

            #création de l'objet final

            emp = Employe(
                matricule=matricule,
                nom=nom,
                prenom=prenom,
                date_naissance=date_naissance,
                genre=genre,
                adresse=adresse,
                mobile=mobile,
                email=email,
                fonction=fonction,
                statut=statut
            )

            try:
                modifier_employe(matricule, emp)
                print("\nModification effectué avec succès.\n")
            except Exception as e:
                print("\nErreur SQL :", e, "\n")
                



        elif choix == "3":
            print("\n--- RECHERCHE D'EMPLOYÉS ---")
            matricule = demander_matricule_existant_e("Entrez le matricule de l'employé à rechercher")
            if matricule:
                table = rechercher_employe(matricule)
                print("\n" + table.get_string() + "\n")

        elif choix == "4":
            print("\n--- CONSULTATION EMPLOYÉ(S) ---")
            matricule = demander_matricule_existant_e("Entrez le matricule de l'employé à consulter")
            if matricule:
                table = consulter_employe(matricule)
                print("\n" + table.get_string() + "\n")

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

            #Récupérer le fournisseur existant 
            fournisseur_actuel = get_fournisseur_by_matricule(matricule)
            if not fournisseur_actuel:
                print("\033[31mfournisseur introuvable.\033[0m\n")
                continue


            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

             # IMPORTANT : remplacer vide == conserver
            matricule = input(f"Matricule [{fournisseur_actuel['matricule']}]: ").strip()
            if matricule == "":
                matricule = fournisseur_actuel["matricule"]

            nom = input(f"Nom [{fournisseur_actuel['nom']}]: ").strip()
            if nom == "":
                nom = fournisseur_actuel["nom"]

            adresse = input(f"Adresse [{fournisseur_actuel['adresse']}]: ").strip()
            if adresse == "":
                adresse = fournisseur_actuel["adresse"]

            mobile = input(f"Mobile [{fournisseur_actuel['mobile']}]: ").strip()
            if mobile == "":
                mobile = fournisseur_actuel["mobile"]

            email = input(f"Email [{fournisseur_actuel['email']}]: ").strip()
            if email == "":
                email = fournisseur_actuel["email"]

            statut = input(f"Statut (1=actif,0=inactif) [{fournisseur_actuel['statut']}]: ").strip()
            if statut not in ("0", "1"):
                statut = fournisseur_actuel["statut"]
            else:
                statut = statut

            #création de l'objet final

            four = Fournisseur(
                matricule=matricule,
                nom=nom,
                adresse=adresse,
                mobile=mobile,
                email=email,
                statut=statut
            )
            try:
                modifier_fournisseur(matricule, four)
                print("\nModification effectuée avec succès.\n")
            except Exception as e:
                print("\nerreur SQL :", e,"\n")
   
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
            ref_produit = demander_ref_produit_existant("Référence du produit à modifier")
            if ref_produit is None:
                continue

            #Récupérer le produit actuel
            produit_actuel = get_produit_by_ref_produit(ref_produit)
            if not produit_actuel:
                print("\033[31mProduit introuvable.\033[0m\n")
                continue

            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            # IMPORTANT : remplacer vide == conserver
            id_fournisseurs = input(f"Identifiant fournisseur [{produit_actuel['id_fournisseurs']}]: ").strip()
            if id_fournisseurs == "":
                id_fournisseurs = produit_actuel["id_fournisseurs"] 


            ref_produit = input(f"Référence [{produit_actuel['ref_produit']}]: ").strip()
            if ref_produit == "":
                ref_produit = produit_actuel["ref_produit"] #conserve la valeur actuelle

            code_atc = input(f"Code atc [{produit_actuel['code_atc']}]: ").strip()
            if code_atc == "":
                code_atc = produit_actuel["code_atc"] 

            nom_commercial = input(f"Nom commercial [{produit_actuel['nom_commercial']}]: ").strip()
            if nom_commercial == "":
                nom_commercial = produit_actuel["nom_commercial"] 

            dci = input(f"Dci [{produit_actuel['dci']}]: ").strip()
            if dci == "":
                dci = produit_actuel["dci"] 

            dosage = input(f"Dosage [{produit_actuel['dosage']}]: ").strip()
            if dosage == "":
                dosage = produit_actuel["dosage"] 

            forme = input(f"Forme [{produit_actuel['forme']}]: ").strip()
            if forme == "":
                forme = produit_actuel["forme"] 

            conditionnement = input(f"Conditionnement [{produit_actuel['conditionnement']}]: ").strip()
            if conditionnement == "":
                conditionnement = produit_actuel["conditionnement"] 

            stock_minimum = input(f"Seuil d'alerte [{produit_actuel['stock_minimum']}]: ").strip()
            if stock_minimum == "":
                stock_minimum = produit_actuel["stock_minimum"] 

            stock_maximum = input(f"Stock initial [{produit_actuel['stock_maximum']}]: ").strip()
            if stock_maximum == "":
                stock_maximum = produit_actuel["stock_maximum"] 

            description_produit = input(f"Description [{produit_actuel['description_produit']}]: ").strip()
            if description_produit == "":
                description_produit = produit_actuel["description_produit"] 

            statut = input(f"Statut (1=actif,0=inactif) [{produit_actuel['statut']}]: ").strip()
            if statut not in ("0", "1"):
                statut = produit_actuel["statut"]
            else:
                statut = statut

            #création de l'objet final

            prod = Produit(
                ref_produit=ref_produit,
                code_atc=code_atc,
                nom_commercial=nom_commercial,
                dci=dci,
                dosage=dosage,
                forme=forme,
                conditionnement=conditionnement,
                stock_minimum=stock_minimum,
                stock_maximum=stock_maximum,
                description_produit=description_produit,
                statut=statut,
                id_fournisseurs=id_fournisseurs

            )

            try:
                modifier_produit(ref_produit, prod)
                print("\nModification effectuée avec succès.\n")
            except Exception as e:
                print("\nErreur SQL :", e,"\n")
                

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
                id_f = input("Identifiant du fournisseur :").strip()

                if rechercher_fournisseur(id_f):
                    break
                else:
                    print("\033[31mErreur !\033[0m id erronné ou non sauvegardé")
                    tentatives += 1

            if tentatives == 3:
                print("Avez-vous oublié l'identifiant ?")
                print("Conseil : consultez la liste des fournisseurs")
                continue

            #statut et observation
            statut = demande_champ("Statut (en cours / annuler / validé)").lower()
            observation = demande_champ("Observation")

            #création de l'objet final

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

            # Vérification ID employé
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

            # Valeurs autorisées pour le statut (doit correspondre à l'ENUM MySQL)
            valeurs_statut = ["libre d'accès", "sous ordonnance"]

            # Saisie du destinataire
            destinataire = ""
            while destinataire not in ["particulier", "professionnel"]:
                destinataire = input("Destinataire (particulier/professionnel) : ").strip().lower()
                if destinataire not in ["particulier", "professionnel"]:
                    print("\033[31mValeur incorrecte. Réessayez !\033[0m")

            # Saisie sécurisée du statut
            statut = ""
            while statut not in valeurs_statut:
                statut = input("Statut (libre d'accès / sous ordonnance) : ").strip()
                if statut not in valeurs_statut:
                    print("\033[31mLa valeur saisie est incorrecte. Réessayez.\033[0m")

            # Saisie de l'observation
            observation = input("Observation : ").strip()

            # Création de l'objet Sortie
            sortie = Sortie(
                id_employes=id_e,
                destinataire=destinataire,
                statut=statut,
                observation=observation
            )

            # Ajout dans la base
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
                id_employes =input("Identifiant de l'employé : ").strip() or None,
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
            print("\nModification effectuée avec succès.\n")    

        elif choix == "3":
            print("\n--- CONSULTER UNE SORTIE ---")

            #Récupération des identifiants valides d'une sortie
            identifiants = demander_identifiants_sortie_existante(
                "ID de la sortie",
                "ID de l'employé"
            )
            if identifiants is None:
                continue
            id_sorties, id_employes = identifiants

            table = consulter_sortie(id_sorties, id_employes)
            print(f"Voici les informations trouvées pour {id_sorties} et {id_employes}")
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
        
        if choix == "1":
            print("\n--- AJOUT D'UNE NOUVELLE LIGNE ENTREE ---")

            #véfication des identifiants del'entree

            identifiants = demander_identifiants_entree_existante(
                "ID de l'entrée",
                "ID du fournisseur"
            )
            if identifiants is None:
                continue
            id_entrees, _ = identifiants

            # Vérification ID produit
            tentatives = 0
            id_produits = None

            while tentatives < 3:
                id_produits = input("ID du produit : ").strip()

                if rechercher_produit(id_produits):
                    break
                else:
                    print("\033[31mErreur ! ID produit incorrect.\033[0m Réessayez.")
                    tentatives += 1

            if tentatives == 3:
                print("Conseil : consultez la liste des produits.")
                continue

            # Champs obligatoires
            numero_lot = demande_champ("Numéro de lot")
            peremption = demande_champ("Date de péremption")
            quantite = demande_champ("Quantité")
            prix_unitaire_entree = demande_champ("Prix unitaire")
            emplacement = demande_champ("Emplacement")

            # Construction de l’objet
            ligne = LigneEntree(
                id_entrees=id_entrees,
                id_produits=id_produits,
                numero_lot=numero_lot,
                peremption=peremption,
                quantite=int(quantite),
                prix_unitaire_entree=float(prix_unitaire_entree),
                emplacement=emplacement
            )

            ajouter_ligne_entree(ligne)
            print("Ligne d'entrée ajoutée avec succès !\n")

        elif choix == "2":
            print("\n--- MODIFICATION D'UNE LIGNE ENTREE ---")

            # Récupération validée des identifiants id_ligne et id_entrees
            identifiants = demander_identifiants_ligne_entree_existante(
                "ID de la ligne",
                "ID de l'entree"
            )

            if identifiants is None:
                continue
            id_ligne, ancien_id_entrees = identifiants

            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            # Saisie des nouveaux champs (None = ne pas modifier)
            nouvelle_id_entrees = input("Nouvel ID de l'entree : ").strip() or None
            nouvelle_id_produits = input("Nouvel ID du produit : ").strip() or None
            nouveau_numero_lot = input("Nouveau numero lot : ").strip() or None
            nouvelle_peremption = input("Nouvelle date de peremption : ").strip() or None

            # Quantité
            while True:
                qte_input = input("Nouvelle quantité : ").strip()
                if not qte_input:
                    nouvelle_quantite = None
                    break
                try:
                    nouvelle_quantite = int(qte_input)
                    break
                except ValueError:
                    print("\033[31mErreur !\033[0m Entrez un nombre entier pour la quantité.")

            # Prix unitaire
            while True:
                prix_input = input("Nouveau prix unitaire : ").strip()
                if not prix_input:
                    nouveau_prix = None
                    break
                try:
                    nouveau_prix = float(prix_input)
                    break
                except ValueError:
                    print("\033[31mErreur !\033[0m Entrez un nombre pour le prix unitaire.")

            # Liste des emplacements valides
            emplacements_valides = ["Z-PMO", "Z-TAC", "Z-ER", "Z-Q"]

            # Saisie + validation
            while True:
                nouvel_emplacement = input(
                    "Nouvel emplacement [Z-PMO], [Z-TAC], [Z-ER], [Z-Q]\nSélectionnez un emplacement: "
                ).strip()

                if not nouvel_emplacement:  
                    nouvel_emplacement = None
                    break

                if nouvel_emplacement and nouvel_emplacement not in emplacements_valides:
                    print("\033[31mCet emplacement n'est pas valide. Modification annulée.\033[0m")
                    continue
                    
                break

            # Validation des nouveaux IDs
            if nouvelle_id_entrees and not rechercher_entree(nouvelle_id_entrees):
                print("\033[31mErreur !\033[0m ID entree invalide. Modification annulée.")
                continue
            if nouvelle_id_produits and not rechercher_produit(nouvelle_id_produits):
                print("\033[31mErreur !\033[0m ID produit invalide. Modification annulée.")
                continue

            # Construction de l’objet LigneEntree 
            ligne_entree = LigneEntree(
            id_entrees=nouvelle_id_entrees,
            id_produits=nouvelle_id_produits,                
            numero_lot=nouveau_numero_lot,
            peremption=nouvelle_peremption,
            quantite=nouvelle_quantite,
            prix_unitaire_entree=nouveau_prix
           )

           # Construction du dictionnaire  le CRUD
            nouveaux_champs = {}
            if ligne_entree.id_entrees is not None:
                nouveaux_champs["id_entrees"] = ligne_entree.id_entrees
            if ligne_entree.id_produits is not None:
                nouveaux_champs["id_produits"] = ligne_entree.id_produits
            if ligne_entree.numero_lot is not None:
                nouveaux_champs["numero_lot"] = ligne_entree.numero_lot
            if ligne_entree.peremption is not None:
                nouveaux_champs["peremption"] = ligne_entree.peremption
            if ligne_entree.quantite is not None:
                nouveaux_champs["quantite"] = ligne_entree.quantite
            if ligne_entree.prix_unitaire_entree is not None:
                nouveaux_champs["prix_unitaire_entree"] = ligne_entree.prix_unitaire_entree
            if ligne_entree.emplacement is not None:
                nouveaux_champs["emplacement"] = ligne_entree.emplacement

            if not nouveaux_champs:
                print("Aucune modification effectuée.")
                continue

            modifier_ligne_entree(id_ligne, ancien_id_entrees, nouveaux_champs)
            print("Ligne entree modifiée avec succès.\n")

        elif choix == "3":
            print("\n--- LISTE DES LIGNES ENTREE ---")
            print(lister_ligne_entree())

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
        if choix == "1":
            print("\n--- AJOUT D'UNE NOUVELLE LIGNE SORTIE ---")

            # Vérification des identifiants de la sortie
            identifiants = demander_identifiants_sortie_existante(
                "ID de la sortie",
                "ID de l'employé"
            )
            if identifiants is None:
                continue
            id_sorties, _ = identifiants
            
            # Vérification ID produit
            tentatives = 0
            id_produits = None

            while tentatives < 3:
                id_produits = input("ID du produit : ").strip()

                if rechercher_produit(id_produits):
                    break
                else:
                    print("\033[31mErreur ! ID produit incorrect.\033[0m Réessayez.")
                    tentatives += 1

            if tentatives == 3:
                print("avez-vous oublié l'identifiant du produit ?")
                print("Conseil : consultez la liste des produits.")
                continue

            # Champs obligatoires
            numero_lot = demande_champ("Numéro de lot")
            peremption = demande_champ("Date de péremption (YYYY-MM-JJ)")
            quantite = demande_champ("Quantité")
            prix_unitaire_vente = demande_champ("Prix unitaire")
            

            # Construction de l’objet
            ligne = LigneSortie (
                id_sorties=id_sorties,
                id_produits=id_produits,
                numero_lot=numero_lot,
                peremption=peremption,
                quantite=int(quantite),
                prix_unitaire_vente=float(prix_unitaire_vente)
            )

            ajouter_ligne_sortie(ligne)
            print("Ligne de sortie ajoutée avec succès !\n")

        elif choix == "2":
            print("\n--- MODIFICATION D'UNE LIGNE SORTIE ---")

            # Récupération validée des identifiants id_ligne et id_sorties
            identifiants = demander_identifiants_ligne_sortie_existante(
                "ID de la ligne",
                "ID de la sortie"
            )

            if identifiants is None:
                continue
            id_ligne, ancien_id_sorties = identifiants

            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            # Saisie des nouveaux champs (None = ne pas modifier)
            nouvelle_id_sorties = input("Nouvel ID de la sortie : ").strip() or None
            nouvelle_id_produits = input("Nouvel ID du produit : ").strip() or None
            nouveau_numero_lot = input("Nouveau numero lot : ").strip() or None
            nouvelle_peremption = input("Nouvelle date de peremption : ").strip() or None

            # Quantité
            while True:
                qte_input = input("Nouvelle quantité : ").strip()
                if not qte_input:
                    nouvelle_quantite = None
                    break
                try:
                    nouvelle_quantite = int(qte_input)
                    break
                except ValueError:
                    print("\033[31mErreur !\033[0m Entrez un nombre entier pour la quantité.")

            # Prix unitaire
            while True:
                prix_input = input("Nouveau prix unitaire : ").strip()
                if not prix_input:
                    nouveau_prix = None
                    break
                try:
                    nouveau_prix = float(prix_input)
                    break
                except ValueError:
                    print("\033[31mErreur !\033[0m Entrez un nombre pour le prix unitaire.")

                # Validation des nouveaux IDs
                if nouvelle_id_sorties and not rechercher_sortie(nouvelle_id_sorties):
                    print("\033[31mErreur !\033[0m ID sortie invalide. Modification annulée.")
                    continue
                if nouvelle_id_produits and not rechercher_produit(nouvelle_id_produits):
                    print("\033[31mErreur !\033[0m ID produit invalide. Modification annulée.")
                    continue

            # Construction de l’objet LigneSortie 
            ligne_sortie = LigneSortie(
            id_sorties=nouvelle_id_sorties,
            id_produits=nouvelle_id_produits,
            numero_lot=nouveau_numero_lot,
            peremption=nouvelle_peremption,
            quantite=nouvelle_quantite,
            prix_unitaire_vente=nouveau_prix
            )

            # Construction du dictionnaire  CRUD
            nouveaux_champs = {}
            if ligne_sortie.id_sorties is not None:
                nouveaux_champs["id_sorties"] = ligne_sortie.id_sorties
            if ligne_sortie.id_produits is not None:
                nouveaux_champs["id_produits"] = ligne_sortie.id_produits
            if ligne_sortie.numero_lot is not None:
                nouveaux_champs["numero_lot"] = ligne_sortie.numero_lot
            if ligne_sortie.peremption is not None:
                nouveaux_champs["peremption"] = ligne_sortie.peremption
            if ligne_sortie.quantite is not None:
                nouveaux_champs["quantite"] = ligne_sortie.quantite
            if ligne_sortie.prix_unitaire_vente is not None:
                nouveaux_champs["prix_unitaire_vente"] = ligne_sortie.prix_unitaire_vente

            if not nouveaux_champs:
                print("Aucune modification effectuée.")
                continue

            modifier_ligne_sortie(id_ligne, ancien_id_sorties, nouveaux_champs)
            print("Ligne sortie modifiée avec succès.\n")


        elif choix == "3":
            print("\n--- LISTE DES LIGNES ENTREE ---")
            print(lister_ligne_sortie())

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



