from Configuration.config import get_connection
from prettytable import PrettyTable

#1. ajouter les details d'une entree
def ajouter_ligne_entree(ligne_entree):
    """
    Ajoute une nouvelle ligne entrée dans la table ligne_entree.
    ligne_entree = objet LigneEntree déjà rempli
    """
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        INSERT INTO ligne_entree(id_entrees, id_produits, numero_lot, peremption, quantite, prix_unitaire_entree, emplacement )
        VALUES(%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        ligne_entree.id_entrees,
        ligne_entree.id_produits,
        ligne_entree.numero_lot,
        ligne_entree.peremption,
        ligne_entree.quantite,
        ligne_entree.prix_unitaire_entree,
        ligne_entree.emplacement
    )
    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()

#2. modifier les informations d'une ligne d'entree 
def modifier_ligne_entree(id_ligne, ancien_id_entrees, nouveaux_champs: dict):
    """
    Met à jour une ligne_entree en permettant aussi de changer id_entrees.
    ancien_id_entrees = valeur actuelle
    nouveaux_champs = champs à modifier
    """
    conn = get_connection()
    cur = conn.cursor()

    set_clause = ", ".join([f"{col}=%s" for col in nouveaux_champs.keys()])
    values = list(nouveaux_champs.values())

    # Ajout des valeurs du WHERE (ancien id_entrees)
    values.append(id_ligne)
    values.append(ancien_id_entrees)

    sql = f"""
        UPDATE ligne_entree
        SET {set_clause}
        WHERE id_ligne=%s AND id_entrees=%s
    """

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()

# 4. Lister toutes les lignes d'une entrées
def lister_ligne_entree():
    conn = get_connection()
    cur = conn.cursor()

    table = PrettyTable(["ID", "ID entree", "ID produit", "Numero lot", "Peremption", "Qte", "PU-e", "Emplacement"])

    sql = """
        SELECT id_ligne, id_entrees, id_produits, numero_lot, peremption, quantite, prix_unitaire_entree, emplacement
        FROM ligne_entree
        ORDER BY id_ligne DESC
    """

    cur.execute(sql)
    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)

    cur.close()
    conn.close()

    return table


def ligne_entree_existe(id_ligne, id_entrees):
    """
    Vérifie si une ligne entrée existe dans la base.
    Retourne True si trouvée, sinon False.
    """
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        SELECT 1 FROM ligne_entree
        WHERE id_ligne=%s AND id_entrees=%s
    """
    cur.execute(sql, (id_ligne, id_entrees))
    resultat = cur.fetchone()

    cur.close()
    conn.close()

    return resultat is not None


