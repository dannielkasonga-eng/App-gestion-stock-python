from Configuration.config import get_connection
from prettytable import PrettyTable

# 1. Ajouter une sortie
def ajouter_sortie(sortie):
    """
    Ajoute une nouvelle sortie dans la table gestion_sortie.
    sortie = objet Sortie déjà rempli
    """

    conn = get_connection()
    cur = conn.cursor()

    sql = """
        INSERT INTO gestion_sortie(
            id_employes, destinataire, statut, observation
        )
        VALUES (%s, %s, %s, %s)
    """

    values = (
        sortie.id_employes,
        sortie.destinataire,
        sortie.statut,
        sortie.observation
    )

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()


# 2. Modifier une sortie
def modifier_sortie(id_sorties, id_employes, nouveaux_champs: dict):
    """
    nouveaux_champs = {"statut": "Validée", "observation": "Sortie confirmée"}
    """

    conn = get_connection()
    cur = conn.cursor()

    set_clause = ", ".join([f"{col}=%s" for col in nouveaux_champs.keys()])
    values = list(nouveaux_champs.values()) + [id_sorties, id_employes]

    sql = f"""
        UPDATE gestion_sortie
        SET {set_clause}
        WHERE id_sorties=%s AND id_employes=%s
    """

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()


# 3. Consulter une sortie (détails avec jointure)
def consulter_sortie(id_sorties, id_employes):
    """
    Retourne une PrettyTable avec les détails complets
    pour une sortie donnée + son employé.
    """

    conn = get_connection()
    cur = conn.cursor()

    table = PrettyTable([
        "ID", "Identifiant", "Employé", "Sortie", "Destinataire",
        "Statut", "Observation", "ID_Produit", "Référence",
        "Nom", "Lot", "Exp", "Qte", "P_U_V"
    ])

    sql = """
        SELECT s.id_sorties AS ID,
               s.id_employes AS identifiant,
               m.matricule AS employes,
               s.date_sortie AS sortie,
               s.destinataire,
               s.statut,
               s.observation,
               ls.id_produits AS ID_produit,
               p.ref_produit AS référence,
               p.nom_commercial AS nom,
               ls.numero_lot AS lot,
               ls.peremption AS Exp,
               ls.quantite AS Qte,
               ls.prix_unitaire_vente AS P_U_V
        FROM gestion_sortie s
        LEFT JOIN ligne_sortie ls
            ON s.id_sorties = ls.id_sorties
        LEFT JOIN employes m
            ON s.id_employes = m.id_employes
        LEFT JOIN produits p
            ON ls.id_produits = p.id_produits
        WHERE s.id_sorties = %s
          AND s.id_employes = %s
    """

    cur.execute(sql, (id_sorties, id_employes))
    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)

    cur.close()
    conn.close()

    return table


# 4. Lister toutes les sorties
def lister_sortie():
    conn = get_connection()
    cur = conn.cursor()

    table = PrettyTable([
        "ID", "Employé", "Date sortie", "Destinataire", "Statut"
    ])

    sql = """
        SELECT id_sorties, id_employes, date_sortie, destinataire, statut
        FROM gestion_sortie
        ORDER BY id_sorties DESC
    """

    cur.execute(sql)
    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)

    cur.close()
    conn.close()

    return table

def employe_valide(id_employes):
    conn = get_connection()
    cur = conn.cursor()

    sql = "SELECT fonction FROM employes WHERE id_employes=%s"
    cur.execute(sql, (id_employes,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return False

    fonction = row[0].lower()

    return fonction in ["Pharmacien adjoint", "Assistant", "Caissier"]

def sortie_existe(id_sorties, id_employes):
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        SELECT 1 FROM gestion_sortie
        WHERE id_sorties=%s AND id_employes=%s
    """
    cur.execute(sql, (id_sorties, id_employes))
    row = cur.fetchone()

    cur.close()
    conn.close()

    return row is not None

def rechercher_sortie(id_sorties, id_employes=None):
    """
    Vérifie si la sortie existe.
    Si id_employes est fourni, vérifie aussi que la sortie appartient à cet employé.
    """
    conn = get_connection()
    cur = conn.cursor()

    if id_employes:
        sql = """
            SELECT id_sorties
            FROM gestion_sortie
            WHERE id_sorties = %s AND id_employes = %s
        """
        cur.execute(sql, (id_sorties, id_employes))
    else:
        sql = """
            SELECT id_sorties
            FROM gestion_sortie
            WHERE id_sorties = %s
        """
        cur.execute(sql, (id_sorties,))

    result = cur.fetchone()
    cur.close()
    conn.close()

    return result is not None

def get_sortie_by_ids(id_sorties, id_employes):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT *
        FROM gestion_sortie
        WHERE id_sorties=%s AND id_employes=%s
    """, (id_sorties, id_employes))

    data = cur.fetchone()

    cur.close()
    conn.close()

    return data


