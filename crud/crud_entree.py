from Configuration.config import get_connection
from prettytable import PrettyTable
from datetime import datetime

#1. ajouter une entrée
def ajouter_entree(entree):
    """
    Ajoute une nouvelle entrée dans la table gestion_entree.
    entree = objet Entree déjà rempli
    """

    conn = get_connection()
    cur = conn.cursor()

    # Si statut 'validé', date_reception = maintenant
    if entree.statut_commande.lower() == "validé":
        date_reception = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        date_reception = None

    date_commande = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # toujours pour la commande

    sql = """
        INSERT INTO gestion_entree (id_fournisseurs, statut_commande, date_commande, date_reception, observation)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        entree.id_fournisseurs,
        entree.statut_commande,
        date_commande,
        date_reception,
        entree.observation
    )

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()


# 2. Modifier une entrée
def modifier_entree(id_entrees, id_fournisseurs, nouveaux_champs: dict):
    
    conn = get_connection()
    cur = conn.cursor()

    set_clause = ", ".join([f"{col}=%s" for col in nouveaux_champs.keys()])
    values = list(nouveaux_champs.values()) + [id_entrees, id_fournisseurs]

    sql = f"""
        UPDATE gestion_entree
        SET {set_clause}
        WHERE id_entrees=%s AND id_fournisseurs=%s
    """
    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()

# 3. Consulter une entrée (détails avec jointure)
def consulter_entree(id_entrees, id_fournisseurs):
    conn = get_connection()
    cur = conn.cursor()

    table = PrettyTable([
        "ID", "ID_f", "Fournisseur", "Date commande", "Statut", "Date reception",
        "Observation", "ID_Produit", "Référence", "Nom", "Lot", "Exp",
        "Qte", "P_U_E", "Emplacement"
    ])

    sql = """
        SELECT e.id_entrees AS ID,
               e.id_fournisseurs,
               f.matricule,
               e.date_commande,
               e.statut_commande,
               e.date_reception,
               e.observation,
               le.id_produits,
               p.ref_produit,
               p.nom_commercial,
               le.numero_lot,
               le.peremption,
               le.quantite AS Qte,
               le.prix_unitaire_entree AS P_U_E,
               le.emplacement AS Section
        FROM gestion_entree e
        LEFT JOIN ligne_entree le
            ON e.id_entrees = le.id_entrees
        LEFT JOIN produits p
            ON le.id_produits = p.id_produits
        LEFT JOIN fournisseurs f
            ON e.id_fournisseurs = f.id_fournisseurs
        WHERE e.id_entrees = %s AND e.id_fournisseurs = %s
    """

    cur.execute(sql, (id_entrees, id_fournisseurs))
    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)

    cur.close()
    conn.close()

    return table

# 4. Lister toutes les entrées
def lister_entree():
    conn = get_connection()
    cur = conn.cursor()

    table = PrettyTable(["ID", "Fournisseur", "Date commande", "Statut", "Date reception", "Observation"])

    sql = """
        SELECT id_entrees, id_fournisseurs, date_commande, statut_commande, date_reception, observation 
        FROM gestion_entree
        ORDER BY id_entrees DESC
    """

    cur.execute(sql)
    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)

    cur.close()
    conn.close()

    return table

def entree_existe(id_entrees, id_fournisseurs):
    conn = get_connection()
    cur = conn.cursor()

    sql = """SELECT id_entrees 
             FROM gestion_entree
             WHERE id_entrees=%s AND id_fournisseurs=%s"""

    cur.execute(sql, (id_entrees, id_fournisseurs))
    result = cur.fetchone()

    cur.close()
    conn.close()

    return result is not None

def rechercher_entree(id_entrees, id_fournisseurs=None):
    """
    Vérifie si l'entrée existe.
    Si id_fournisseurs est fourni, vérifie aussi que l'entrée appartient à ce fournisseur.
    """
    conn = get_connection()
    cur = conn.cursor()

    if id_fournisseurs:
        sql = """
            SELECT id_entrees
            FROM gestion_entree
            WHERE id_entrees = %s AND id_fournisseurs = %s
        """
        cur.execute(sql, (id_entrees, id_fournisseurs))
    else:
        sql = """
            SELECT id_entrees
            FROM gestion_entree
            WHERE id_entrees = %s
        """
        cur.execute(sql, (id_entrees,))

    result = cur.fetchone()
    cur.close()
    conn.close()

    return result is not None


