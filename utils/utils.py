from crud.crud_produit import rechercher_produit
from crud.crud_employe import rechercher_employe
from crud.crud_fournisseur import rechercher_fournisseur
from crud.crud_entree import entree_existe
from crud.crud_sortie import sortie_existe
from crud.crud_produit import id_produits_existe
from crud.crud_ligne_entree import ligne_entree_existe
from crud.crud_ligne_sortie import ligne_sortie_existe

def demande_champ(label, obligatoire=True):
    """
    Demande à l'utilisateur de saisir une valeur pour un champ.
    Si le champ est obligatoire, empêche la saisie vide.
    """
    while True:
        valeur = input(f"{label} : ").strip()
        if obligatoire and not valeur:
            print("\033[1;31mCe champ est obligatoire ! Veuillez le remplir avant de continuer.\033[0m\n")
        else:
            return valeur
        
        
       
def demander_matricule_existant_e(label):
    tentatives = 0
    while tentatives < 3:
        matricule = input(f"{label} : ").strip()

        if len(matricule) != 10:
            print("Le matricule d'un employé est strictement constitué de 10 caractères.\n")
            tentatives += 1
            continue

        table = rechercher_employe(matricule)
        if len(table._rows) > 0:
            return matricule
        else:
            print("Matricule erroné. Réessayez.\n")
            tentatives += 1

    print("Avez-vous oublié le matricule ?")
    print("Conseil : Consultez la liste des employés sauvegardés.\n")
    return None

def demander_matricule_existant_f(label):
    tentatives = 0
    while tentatives < 3:
        matricule = input(f"{label} : ").strip()

        if len(matricule) != 14:
            print("Le matricule d'un fournisseur est strictement constitué de 14 caractères.\n")
            tentatives += 1
            continue

        table = rechercher_fournisseur(matricule)
        if len(table._rows) > 0:
            return matricule
        else:
            print("Matricule erroné. Réessayez.\n")
            tentatives += 1

    print("Avez-vous oublié le matricule ?")
    print("Conseil : Consultez la liste des fournisseurs sauvegardés.\n")
    return None


def demander_ref_produit_existant(label):
    tentatives = 0

    while tentatives < 3:
        ref = input(f"{label} : ").strip()

        # Doit faire 6 caractères
        if len(ref) != 6:
            print("Une référence produit doit contenir exactement 6 caractères.\n")
            tentatives += 1
            continue

        # Vérifier existence en base
        table = rechercher_produit(ref)
        if len(table._rows) > 0:
            return ref

        print("Référence introuvable. Réessayez.\n")
        tentatives += 1

    print("Avez-vous oublié la référence produit ?")
    print("Conseil : consultez la liste des produits sauvegardés.\n")
    return None

def demander_id_produit_existant(label):
    tentatives = 0

    while tentatives < 3:
        valeur = input(f"{label} : ").strip()

        # Vérifier que la valeur est un entier
        if not valeur.isdigit():
            print("Un identifiant est un nombre entier.\n")
            tentatives += 1
            continue

        id_produits = int(valeur)

        # Vérifier existence via ta fonction
        if id_produits_existe(id_produits):
            return id_produits

        print("Identifiant produit introuvable. Réessayez.\n")
        tentatives += 1

    print("Avez-vous oublié l'id produit ?")
    print("Conseil : consultez la liste des produits sauvegardés.\n")
    return None



def demander_identifiants_entree_existante(label_entree, label_fournisseur):
    id_entrees = input(f"{label_entree} : ").strip()
    id_fournisseurs = input(f"{label_fournisseur} : ").strip()

    if not entree_existe(id_entrees, id_fournisseurs):
        print("\033[31mEntrée non sauvegardée\033[0m")
        print("\033[31mConseil : Consultez la liste des entrées\033[0m")
        return None

    return id_entrees, id_fournisseurs

def demander_identifiants_sortie_existante(label_sortie, label_employe):
    id_sorties = input(f"{label_sortie} : ").strip()
    id_employes = input(f"{label_employe} : ").strip()

    if not sortie_existe(id_sorties, id_employes):
        print("\033[31mSortie non sauvegardée\033[0m")
        print("\033[31mConseil : Consultez la liste des sorties\033[0m")
        return None

    return id_sorties, id_employes



def demander_identifiants_ligne_entree_existante(msg_ligne, msg_entree):
    """
    Demande id_ligne + id_entrees et vérifie l'existence.
    Retourne un tuple (id_ligne, id_entrees) ou None si invalide.
    """

    id_ligne = input(f"{msg_ligne} : ").strip()
    id_entrees = input(f"{msg_entree} : ").strip()

    if not id_ligne.isdigit() or not id_entrees.isdigit():
        print("Erreur : les identifiants doivent être numériques.")
        return None

    id_ligne = int(id_ligne)
    id_entrees = int(id_entrees)

    if not ligne_entree_existe(id_ligne, id_entrees):
        print("Erreur : cette ligne entrée n’est pas enregistrée.")
        print("Conseil : consultez la liste des lignes entrées.")
        return None

    return id_ligne, id_entrees

def demander_identifiants_ligne_sortie_existante(msg_ligne, msg_sortie):
    """
    Demande id_ligne + id_sorties et vérifie l'existence.
    Retourne un tuple (id_ligne, id_sorties) ou None si invalide.
    """

    id_ligne = input(f"{msg_ligne} : ").strip()
    id_sorties = input(f"{msg_sortie} : ").strip()

    if not id_ligne.isdigit() or not id_sorties.isdigit():
        print("Erreur : les identifiants doivent être numériques.")
        return None

    id_ligne = int(id_ligne)
    id_sorties = int(id_sorties)

    if not ligne_sortie_existe(id_ligne, id_sorties):
        print("Erreur : cette ligne sortie n’est pas enregistrée.")
        print("Conseil : consultez la liste des lignes de sorties.")
        return None

    return id_ligne, id_sorties


