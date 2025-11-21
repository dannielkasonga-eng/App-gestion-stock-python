from Configuration.config import get_connection
from prettytable import PrettyTable

# 1. ajouter produit
def ajouter_produit(produit):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO produits(
            ref_produit, code_atc, nom_commercial, dci,
            description_produit, stock_minimum, stock_maximum,
            statut
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        produit.ref_produit,
        produit.code_atc,
        produit.nom_commercial,
        produit.dci,
        produit.description_produit,
        produit.stock_minimum,
        produit.stock_maximum,
        produit.statut
    )

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()


# 2. modifier produit
def modifier_produit(ref_produit, produit):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        UPDATE produits SET
            code_atc=%s,
            nom_commercial=%s,
            dci=%s,
            description_produit=%s,
            stock_minimum=%s,
            stock_maximum=%s,
            statut=%s
        WHERE ref_produit=%s
    """

    values = (
        produit.code_atc,
        produit.nom_commercial,
        produit.dci,
        produit.description_produit,
        produit.stock_minimum,
        produit.stock_maximum,
        produit.statut,
        ref_produit
    )

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()

#3. rechercher produit
def rechercher_produit(ref_produit):
    conn = get_connection()
    cursor = conn.cursor()

    table = PrettyTable([
        "Réf", "ATC", "Nom", "DCI", "Description"
    ])

    sql = """
        SELECT ref_produit, code_atc, nom_commercial,
               dci, description_produit
        FROM produits
        WHERE ref_produit = %s
    """

    cursor.execute(sql, (ref_produit,))
    row = cursor.fetchone()

    if row:
        table.add_row(row)

    cursor.close()
    conn.close()

    return table


# 4. consulter produit (toutes infos + entrées + sorties)
def consulter_produit(ref_produit):
    conn = get_connection()
    cursor = conn.cursor()

    table = PrettyTable([
        "ID", "Référence", "ATC", "Nom", "DCI",
        "Seuil", "Stock init",
        "ID Entree", "Lot E", "Exp E", "Qte E", "PU Entree", "Section",
        "ID Sortie", "Lot S", "Exp S", "Qte S", "PU Sortie"
    ])

    sql = """
        SELECT p.id_produits AS ID,
               p.ref_produit AS référence,
               p.code_atc AS atc,
               p.nom_commercial AS nom,
               p.dci,
               p.stock_minimum AS seuil_alerte,
               p.stock_maximum AS stock_initial,
               le.id_entrees,
               le.numero_lot,
               le.peremption,
               le.quantite,
               le.prix_unitaire_entree,
               le.emplacement,
               ls.id_sorties,
               ls.numero_lot,
               ls.peremption,
               ls.quantite,
               ls.prix_unitaire_vente
        FROM produits p
        LEFT JOIN ligne_entree le
            ON p.id_produits = le.id_produits
        LEFT JOIN ligne_sortie ls
            ON p.id_produits = ls.id_produits
        WHERE p.ref_produit = %s
    """

    cursor.execute(sql, (ref_produit,))
    rows = cursor.fetchall()

    for row in rows:
        table.add_row(row)

    cursor.close()
    conn.close()

    return table

# 5. desactiver produit
def desactiver_produit(ref_produit):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "UPDATE produits SET statut=0 WHERE ref_produit=%s"

    cursor.execute(sql, (ref_produit,))
    conn.commit()

    cursor.close()
    conn.close()


# 6. activer produit
def activer_produit(ref_produit):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "UPDATE produits SET statut=1 WHERE ref_produit=%s"

    cursor.execute(sql, (ref_produit,))
    conn.commit()

    cursor.close()
    conn.close()


# 7. lister tous les produits
def lister_produits():
    conn = get_connection()
    cursor = conn.cursor()

    table = PrettyTable([
        "ID", "Réf", "ATC", "Nom", "DCI",
        "Description", "Stock min", "Stock max", "Statut"
    ])

    sql = """
        SELECT id_produits, ref_produit, code_atc, nom_commercial,
               dci, description_produit, stock_minimum,
               stock_maximum, statut
        FROM produits
    """

    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        table.add_row(row)

    cursor.close()
    conn.close()

    return table

def ref_produit_existe(ref):
    """
    Vérifie si une référence produit existe en base.
    Retourne True ou False.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM produits WHERE ref_produit = %s", (ref,))
    exists = cur.fetchone()[0] > 0
    cur.close()
    conn.close()
    return exists

def id_produits_existe(id_prod):
    conn = get_connection()
    cur = conn.cursor()

    sql = "SELECT COUNT(*) FROM produits WHERE id_produits = %s"
    cur.execute(sql, (id_prod,))
    existe = cur.fetchone()[0] > 0

    cur.close()
    conn.close()
    return existe
