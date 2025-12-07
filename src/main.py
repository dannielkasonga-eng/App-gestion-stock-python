from Configuration.config import get_connection
from utils.utils import demande_champ
from utils.utils import demander_matricule_existant_e
from utils.utils import demander_matricule_existant_f
from utils.utils import demander_ref_produit_existant
from utils.utils import demander_id_fournisseur_existant
from utils.utils import demander_identifiants_entree_existante
from utils.utils import demander_identifiants_sortie_existante
from utils.utils import demander_identifiants_ligne_entree_existante
from utils.utils import demander_identifiants_ligne_sortie_existante

#Importation du module employe et fonctions crud employe

from crud.crud_employe import (
    ajouter_employe, modifier_employe, consulter_employe,
    rechercher_employe, lister_employes, desactiver_employe,
    activer_employe, get_employe_by_matricule

 )
from modules.employe import Employe 

#importation du module fournisseur et fonctions crud fournisseurs

from crud.crud_fournisseur import (
    ajouter_fournisseur, modifier_fournisseur, consulter_fournisseur,
    rechercher_fournisseur, lister_fournisseurs, desactiver_fournisseur,
    activer_fournisseur, get_fournisseur_by_matricule  
)
from modules.fournisseur import Fournisseur

#importation du module produit et fonctions crud produit

from crud.crud_produit import (
    ajouter_produit, modifier_produit, consulter_produit,
    rechercher_produit, lister_produits, desactiver_produit,
    activer_produit, id_produits_existe, get_produit_by_ref_produit
)
from modules.produit import Produit


#importation du module entree et fonctions crud entree

from crud.crud_entree import (
    ajouter_entree, modifier_entree, consulter_entree,
    lister_entree, get_entree_by_ids
)
from modules.entree import Entree

#importation du module sortie et fonctions crud sortie

from crud.crud_sortie import (
    ajouter_sortie, modifier_sortie, consulter_sortie,
    lister_sortie, employe_valide, get_sortie_by_ids
)
from modules.sortie import Sortie

#Importation du module ligne_entree et fonctions crud ligne_entree

from crud.crud_ligne_entree import (
    ajouter_ligne_entree, modifier_ligne_entree, lister_ligne_entree,
    get_ligne_entree_by_ids
)
from crud.crud_produit import rechercher_produit
from modules.ligne_entree import LigneEntree

from crud.crud_ligne_sortie import (
    ajouter_ligne_sortie, modifier_ligne_sortie, lister_ligne_sortie,
    get_ligne_sortie_by_ids
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
            print("\n--- RECHERCHE D'UN FOURNISSEUR ---")
            matricule = demander_matricule_existant_f("Entrez le matricule fournisseur à rechercher")
            if matricule:
                table= rechercher_fournisseur(matricule)
                print("\n" + table.get_string() + "\n")

        elif choix == "4":
            print("\n--- CONSULTATION D'UN FOURNISSEUR ---")
            matricule = demander_matricule_existant_f("Entrez le matricule du fournisseur à consulter")
            if matricule:
                table = consulter_fournisseur(matricule)
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

            #ID fournisseur déjà vérifié dans une fonction utilitaire
            id_fournisseurs = demander_id_fournisseur_existant("ID du fournisseur")
            if id_fournisseurs is None:
                continue

            #Référence produit – doit faire 6 caractères
            while True:
                ref_produit = demande_champ("Référence produit").strip()
                if len(ref_produit) == 6:
                    break
                print("Erreur : une référence produit doit contenir EXACTEMENT 6 caractères.\n")

            #Code ATC – doit faire 7 caractères
            while True:
                code_atc = demande_champ("Code ATC").strip()
                if len(code_atc) == 7:
                    break
                print("Erreur : un code ATC doit contenir EXACTEMENT 7 caractères.\n")

            #Champs libres (pas de contraintes)
            nom_commercial = demande_champ("Nom commercial")
            dci = demande_champ("DCI")
            dosage =demande_champ("Dosage")
            forme =demande_champ("Forme")
            conditionnement =demande_champ("Conditionnement")

            #Stock minimum – doit être un entier
            while True:
                stock_minimum = demande_champ("Stock minimum").strip()
                if stock_minimum.isdigit():
                    stock_minimum = int(stock_minimum)
                    break
                print("Erreur : le stock minimum doit être un nombre entier.\n")

            #Stock maximum – doit être un entier
            while True:
                stock_maximum = demande_champ("Stock maximum").strip()
                if stock_maximum.isdigit():
                    stock_maximum = int(stock_maximum)
                    break
                print("Erreur : le stock maximum doit être un nombre entier.\n")
            description_produit = demande_champ("Description")

            #Création de l’objet produit avec les valeurs validées
            prod = Produit(
                id_fournisseurs=id_fournisseurs,
                ref_produit=ref_produit,
                code_atc=code_atc,
                nom_commercial=nom_commercial,
                dci=dci,
                dosage=dosage,
                forme=forme,
                conditionnement=conditionnement,
                stock_minimum=stock_minimum,
                stock_maximum=stock_maximum,
                description_produit=description_produit
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
            else:
                try:
                    stock_minimum = int(stock_minimum)
                except ValueError:
                     print("Le seuil d'alerte doit être un nombre entier. Valeur conservée.")
                     stock_minimum = produit_actuel["stock_minimum"]

            stock_maximum = input(f"Stock initial [{produit_actuel['stock_maximum']}]: ").strip()
            if stock_maximum == "":
                stock_maximum = produit_actuel["stock_maximum"]
            else:
                try:
                    stock_maximum = int(stock_maximum)
                except ValueError:
                    print("Le stock initial doit être un nombre entier. Valeur conservée") 
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
        choix = input("Choisissez une option :").strip()
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
            statut = demande_champ("Statut (En cours / Validee / Annulee )").strip()
            observation = demande_champ("Observation").strip()

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
            # Étape 1 : Vérifier que l’entrée existe bien
            identifiants = demander_identifiants_entree_existante(
                "ID de l'entrée",
                "ID du fournisseur"
                )
            if identifiants is None:
                continue
            id_entrees, id_fournisseurs = identifiants

            # Récupération de l'entrée actuelle 
            entree_actuelle = get_entree_by_ids(id_entrees, id_fournisseurs)
            if not entree_actuelle:
                print("\033[31mEntrée introuvable.\033[0m\n")
                continue
            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            # --- Nouveau champ 1 ---
            id_fournisseur_new = input(f"ID fournisseur [{entree_actuelle['id_fournisseurs']}]: ").strip()
            if id_fournisseur_new == "":
                id_fournisseur_new = entree_actuelle["id_fournisseurs"]

            # --- Nouveau champ 2 ---
            statut_new = input(f"Statut commande (En cours / Validee / Annulee)[{entree_actuelle['statut_commande']}]: ").strip()
            if statut_new == "":
                statut_new = entree_actuelle["statut_commande"]

            # --- Nouveau champ 3 ---
            observation_new = input(f"Observation [{entree_actuelle['observation']}]: ").strip()
            if observation_new == "":
                observation_new = entree_actuelle["observation"]

            # Création de l’objet mise à jour
            entree_modifiee = Entree(
                id_entrees=id_entrees,
                id_fournisseurs=id_fournisseur_new,
                statut_commande=statut_new,
                observation=observation_new
                )

            # Exécution du CRUD 
            try:
                modifier_entree(id_entrees, id_fournisseurs, entree_modifiee)
                print("\nEntrée modifiée avec succès.\n")
            except Exception as e:
                print("\nErreur SQL :", e, "\n")


        elif choix == "3":
            print("\n--- CONSULTER UNE ENTREE ---")

            #Récupération des identifiants valides d'une entree
            identifiants = demander_identifiants_entree_existante(
                "ID de l' entree",
                "ID du fournisseur"
            )
            if identifiants is None:
                continue
            id_entrees, id_fournisseurs = identifiants

            table = consulter_entree(id_entrees, id_fournisseurs)
            print(f"Voici les informations trouvées pour {id_entrees} et {id_fournisseurs}")
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
            # Vérification ID employé
            print("Note : seuls le pharmacien adjoint, assistant et caissier peuvent effectuer une sortie.\n")
            tentatives = 0
            id_e = None

            while tentatives < 3:
                id_e = input("Identifiant de l'employé : ").strip()

                if employe_valide(id_e):
                    break
                else:
                    print("\033[31mErreur !\033[0m id erronné ou non sauvegardé. Réessayez :")
                    tentatives += 1

                if tentatives == 3:
                    print("Avez-vous oublié l'identifiant ?")
                    print("Conseil : consultez la liste des employés")
                    continue

            # Saisie du destinataire
            destinataire = ""
            while destinataire not in ["Particulier", "Professionnel"]:
                destinataire = input("Destinataire (Particulier/Professionnel) : ").strip().lower()
                if destinataire not in ["Particulier", "Professionnel"]:
                    print("\033[31mValeur incorrecte. Réessayez !\033[0m")

            # Statut et observation
            statut = demande_champ("Statut (Vente libre\ Sous ordonnance)").strip()
            observation = demande_champ("obseravtion").strip()
            

            # Création de l'objet final
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
            # Récupération de la sortie actuelle 
            sortie_actuelle = get_sortie_by_ids(id_sorties, id_employes)
            if not sortie_actuelle:
                print("\033[31mSortie introuvable.\033[0m\n")
                continue

            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            # --- Nouveau champ 1 ---
            id_employe_new = input(f"ID employe [{sortie_actuelle['id_employes']}]: ").strip()
            if id_employe_new == "":
                id_employe_new = sortie_actuelle["id_employes"]

            # --- Nouveau champ 2 ---
            statut_new = input(f"Statut de la sortie (Vente libre / Sous ordonnance)[{sortie_actuelle['statut']}]: ").strip()
            if statut_new == "":
                statut_new = sortie_actuelle["statut"]

            # --- Nouveau champ 3 ---
            observation_new = input(f"Observation [{sortie_actuelle['observation']}]: ").strip()
            if observation_new == "":
                observation_new = sortie_actuelle["observation"]

            # Création de l’objet mise à jour
            sortie_modifiee = Sortie(
                id_sorties=id_sorties,
                id_employes=id_employe_new,
                statut=statut_new,
                observation=observation_new
                )

            # Exécution du CRUD 
            try:
                modifier_sortie(id_sorties, id_employes, sortie_modifiee)
                print("\nSortie modifiée avec succès.\n")
            except Exception as e:
                print("\nErreur SQL :", e, "\n")    

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
        choix = input("Choisissez une option :").strip()
        
        if choix == "1":
            print("\n--- AJOUT D'UNE NOUVELLE LIGNE ENTREE ---")

            #véfication de l'existence de l'entrée dans la base de données

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
                print("avez-vous oublié l'identifiant du produit ?")
                print("Conseil : consultez la liste des produits.")
                continue

            # Champs obligatoires
            numero_lot = demande_champ("Numéro de lot")
            peremption = demande_champ("Date de péremption (YYYY-MM-JJ)")
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
            print("Ligne de l'entrée ajoutée avec succès !\n")

        elif choix == "2":
            print("\n--- MODIFICATION D'UNE LIGNE ENTREE ---")

            # Récupération validée des identifiants id_ligne et id_entrees
            identifiants = demander_identifiants_ligne_entree_existante(
                "ID de la ligne",
                "ID de l'entree"
            )

            if identifiants is None:
                continue
            id_ligne, id_entrees = identifiants

            # Récupération de l'entrée actuelle 
            ligne_actuelle = get_ligne_entree_by_ids(id_ligne, id_entrees)
            if not ligne_actuelle:
                print("\033[31mLigne introuvable.\033[0m\n")
                continue

            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            # --- Nouveau champ 1 ---
            id_entree_new = input(f"Identifiant de l'entrée [{ligne_actuelle['id_entrees']}]: ").strip()
            if id_entree_new == "":
                id_entree_new = ligne_actuelle["id_entrees"]

            # --- Nouveau champ 2 ---
            id_produit_new = input(f"ID produit [{ligne_actuelle['id_produits']}]: ").strip()
            if id_produit_new == "":
                id_produit_new = ligne_actuelle["id_produits"]

            # --- Nouveau champ 3 ---
            numero_lot_new = input(f"Numero lot [{ligne_actuelle['numero_lot']}]: ").strip()
            if numero_lot_new == "":
                numero_lot_new = ligne_actuelle["numero_lot"]

            # --- Nouveau champ 4 ---
            peremption_new = input(f"Peremption [{ligne_actuelle['peremption']}]: ").strip()
            if peremption_new == "":
                peremption_new = ligne_actuelle["peremption"]

            # --- Nouveau champ 5 ---
            quantite_new = input(f"Quantité [{ligne_actuelle['quantite']}]: ").strip()
            if quantite_new == "":
                quantite_new = ligne_actuelle["quantite"]
            else:
                try:
                    quantite_new = int(quantite_new)
                except ValueError:
                    print("La quantite de produits doit-être en entier. Valeur conservée")
                    quantite_new = ligne_actuelle["quantite"]

            # --- Nouveau champ 6
            prix_unitaire_entree_new = input(f"Prix unitaire [{ligne_actuelle['prix_unitaire_entree']}]: ").strip()
            if prix_unitaire_entree_new == "":
                prix_unitaire_entree_new = ligne_actuelle["prix_unitaire_entree"]
            else:
                try:
                    prix_unitaire_entree_new = float(prix_unitaire_entree_new)
                except ValueError:
                    print("Le prix unitaire doit-être un decimal. valeur conservé") 
                    prix_unitaire_entree_new = ligne_actuelle["prix_unitaire_entree"]

            emplacement_new = input(f"Emplacement (Z-PMO /Z-TAC /Z-ER /Z-Q) [{ligne_actuelle['emplacement']}]: ").strip()
            if emplacement_new == "":
                emplacement_new = ligne_actuelle["emplacement"]

            # Création de l’objet final
            ligne_entree_modifiee = LigneEntree(
                id_ligne=id_ligne,
                id_entrees=id_entree_new,
                id_produits=id_produit_new,
                numero_lot=numero_lot_new,
                peremption=peremption_new,
                quantite=quantite_new,
                prix_unitaire_entree=prix_unitaire_entree_new,
                emplacement=emplacement_new
                )
            
            # Exécution du CRUD 
            try:
                modifier_ligne_entree(id_ligne, id_entrees, ligne_entree_modifiee)
                print("\nLigne entree modifiée avec succès.\n")
            except Exception as e:
                print("\nErreur SQL :", e, "\n")

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
        choix = input("Choisissez une option :").strip()
        if choix == "1":
            print("\n--- AJOUT D'UNE NOUVELLE LIGNE SORTIE ---")

            # Vérification de l'existence de la sortie dans la base de données
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
            print("Ligne de la +sortie ajoutée avec succès !\n")

        elif choix == "2":
            print("\n--- MODIFICATION D'UNE LIGNE SORTIE ---")

            # Récupération validée des identifiants id_ligne et id_sorties
            identifiants = demander_identifiants_ligne_sortie_existante(
                "ID de la ligne",
                "ID de la sortie"
            )

            if identifiants is None:
                continue
            id_ligne, id_sorties = identifiants

            # Récupération de l'entrée actuelle 
            ligne_actuelle = get_ligne_sortie_by_ids(id_ligne, id_sorties)
            if not ligne_actuelle:
                print("\033[31mLigne introuvable.\033[0m\n")
                continue

            print("\nLaissez vide un champ pour conserver la valeur actuelle.\n")

            # --- Nouveau champ 1 ---
            id_sortie_new = input(f"Identifiant de la sortie [{ligne_actuelle['id_sorties']}]: ").strip()
            if id_sortie_new == "":
                id_sortie_new = ligne_actuelle["id_sorties"]

            # --- Nouveau champ 2 ---
            id_produit_new = input(f"ID produit [{ligne_actuelle['id_produits']}]: ").strip()
            if id_produit_new == "":
                id_produit_new = ligne_actuelle["id_produits"]

            # --- Nouveau champ 3 ---
            numero_lot_new = input(f"Numero lot [{ligne_actuelle['numero_lot']}]: ").strip()
            if numero_lot_new == "":
                numero_lot_new = ligne_actuelle["numero_lot"]

            # --- Nouveau champ 4 ---
            peremption_new = input(f"Peremption [{ligne_actuelle['peremption']}]: ").strip()
            if peremption_new == "":
                peremption_new = ligne_actuelle["peremption"]

            # --- Nouveau champ 5 ---
            quantite_new = input(f"Quantité [{ligne_actuelle['quantite']}]: ").strip()
            if quantite_new == "":
                quantite_new = ligne_actuelle["quantite"]
            else:
                try:
                    quantite_new = int(quantite_new)
                except ValueError:
                    print("La quantite de produits doit-être en entier. Valeur conservée")
                    quantite_new = ligne_actuelle["quantite"]

            # --- Nouveau champ 6
            prix_unitaire_vente_new = input(f"Prix unitaire [{ligne_actuelle['prix_unitaire_vente']}]: ").strip()
            if prix_unitaire_vente_new == "":
                prix_unitaire_vente_new = ligne_actuelle["prix_unitaire_vente"]
            else:
                try:
                    prix_unitaire_vente_new = float(prix_unitaire_vente_new)
                except ValueError:
                    print("Le prix unitaire doit-être un decimal. valeur conservé") 
                    prix_unitaire_vente_new = ligne_actuelle["prix_unitaire_vente"]

            # Création de l’objet final
            ligne_sortie_modifiee = LigneEntree(
                id_ligne=id_ligne,
                id_sorties=id_sortie_new,
                id_produits=id_produit_new,
                numero_lot=numero_lot_new,
                peremption=peremption_new,
                quantite=quantite_new,
                prix_unitaire_vente=prix_unitaire_vente_new,
                )
            
            # Exécution du CRUD 
            try:
                modifier_ligne_sortie(id_ligne, id_sorties, ligne_sortie_modifiee)
                print("\nLigne sortie modifiée avec succès.\n")
            except Exception as e:
                print("\nErreur SQL :", e, "\n")


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



