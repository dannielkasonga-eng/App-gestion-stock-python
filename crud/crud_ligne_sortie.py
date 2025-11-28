from Configuration.config import get_connection
from prettytable import PrettyTable

#1. ajouter une nouvelle ligne d'une sortie
def ajouter_ligne_sortie(ligne_sortie):
    """
    Ajoute une nouvelle ligne d'une sortie dans la table ligne_sortie
    ligne_sortie = objet LigneSortie déjà rempli
    """
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        INSERT INTO ligne_sortie(id_sorties, id_produits, numero_lot, peremption, quantite, prix_unitaire_vente)
        VALUES (%s, %s, %s, %s, %s, %s)
    
    """
    values = (
        ligne_sortie.id_sorties,
        ligne_sortie.id_produits,
        ligne_sortie.numero_lot,
        ligne_sortie.peremption,
        ligne_sortie.quantite,
        ligne_sortie.prix_unitaire_vente
    )

    cur.execute(sql, values)
    conn.commit()

    cur.close
    conn.close

#2. modifier les informations d'une ligne de sortie
def modifier_ligne_sortie(id_ligne, ancien_id_sorties, nouveaux_champs: dict):
    """
    Met à jour une ligne_sortie en permettant aussi de changer id_sorties.
    ancien_id_sorties = valeur actuelle
    nouveaux_champs = champs à modifier
    """
    conn = get_connection()
    cur = conn.cursor()

    set_clause = ", ".join([f"{col}=%s" for col in nouveaux_champs.keys()])
    values = list(nouveaux_champs.values())

    # Ajout des valeurs du WHERE (ancien id_sorties)
    values.append(id_ligne)
    values.append(ancien_id_sorties)

    sql = f"""
        UPDATE ligne_sortie
        SET {set_clause}
        WHERE id_ligne=%s AND id_sorties=%s
    """

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()


#3. lister toutes les lignes d'une sortie
def lister_ligne_sortie():
    conn = get_connection()
    cur = conn.cursor()

    table = PrettyTable(["ID", "ID sortie", "ID produit", "Numero lot", "peremption", "Qte", "P_U_V"])

    sql = """
        SELECT id_ligne, id_sorties, id_produits, numero_lot, peremption, quantite, prix_unitaire_vente
        FROM ligne_sortie
        ORDER BY id_ligne DESC
    """

    cur.execute(sql)
    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)

    cur.close()
    conn.close()

    return table

def ligne_sortie_existe(id_ligne, id_sorties):
    """
    Vérifie si une ligne sortie existe dans la base.
    Retourne True si trouvée, sinon False.
    """
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        SELECT 1 FROM ligne_sortie
        WHERE id_ligne=%s AND id_sorties=%s
    """
    cur.execute(sql, (id_ligne, id_sorties))
    resultat = cur.fetchone()

    cur.close()
    conn.close()

    return resultat is not None
