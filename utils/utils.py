from crud.crud_produit import rechercher_produit
from crud.crud_employe import rechercher_employe
from crud.crud_fournisseur import rechercher_fournisseur
from crud.crud_entree import entree_existe

@staticmethod
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

        table = rechercher_employe([matricule])
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
        table = rechercher_fournisseur([matricule])
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

    if not entree_existe(id_sorties, id_employes):
        print("\033[31mSortie non sauvegardée\033[0m")
        print("\033[31mConseil : Consultez la liste des sorties\033[0m")
        return None

    return id_sorties, id_employes
