#creation des fonctions crud du module fournisseur
from Configuration.config import get_connection
from prettytable import PrettyTable


# 1. Ajouter un fournisseur
def ajouter_fournisseur(fournisseur):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO fournisseurs 
        (matricule, nom, adresse, mobile, email, statut)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (
        fournisseur.matricule,
        fournisseur.nom,
        fournisseur.adresse,
        fournisseur.mobile,
        fournisseur.email,
        fournisseur.statut
    ))

    conn.commit()
    cursor.close()
    conn.close()



# 2. Modifier un fournisseur
def modifier_fournisseur(matricule, fournisseur):
    """
    Modifie un fournisseur existant.
    matricule = matricule du fournisseur cible
    fournisseur = objet Fournisseur avec les nouvelles valeurs
    """
    conn = get_connection()
    cur = conn.cursor()

    sql = """
        UPDATE fournisseurs 
        SET matricule=%s, nom=%s, adresse=%s, mobile=%s, email=%s, statut=%s
        WHERE matricule=%s
    """

    values = (
        fournisseur.matricule,
        fournisseur.nom,
        fournisseur.adresse,
        fournisseur.mobile,
        fournisseur.email,
        fournisseur.statut,
        matricule
    )

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()



# 3. Rechercher un ou plusieurs fournisseurs (infos restreintes)
def rechercher_fournisseur(matricule):
    conn = get_connection()
    cur = conn.cursor()

    table = PrettyTable(["Matricule", "Nom", "Adresse", "Mobile"])

    sql = """
        SELECT matricule, nom, adresse, mobile
        FROM fournisseurs 
        WHERE matricule = %s
    """

    cur.execute(sql, (matricule,))
    row = cur.fetchone()
    if row:
        table.add_row(row)

    cur.close()
    conn.close()
    return table



# 4. Consulter un ou plusieurs fournisseurs (détails complets + entrées)
def consulter_fournisseur(matricule):
    conn = get_connection()
    cursor = conn.cursor()

    table = PrettyTable([
        "ID", "Matricule", "Nom", "Adresse", "Mobile", "Email",
        "Statut", "Date commande", "Statut commande", "Date livraison"
    ])

    sql = """
        SELECT f.id_fournisseurs AS ID,
               f.matricule AS matricule,
               f.nom, 
               f.adresse,
               f.mobile,
               f.email,
               f.statut,
               e.date_commande,
               e.statut_commande,
               e.date_reception AS Date_livraison
        FROM fournisseurs f
        LEFT JOIN gestion_entree e
        ON f.id_fournisseurs = e.id_fournisseurs
        WHERE f.matricule = %s
    """

    cursor.execute(sql, (matricule,))
    rows = cursor.fetchall()
    for row in rows:
        table.add_row(row)

    cursor.close()
    conn.close()
    return table



# 5. Désactiver un fournisseur
def desactiver_fournisseur(matricule):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "UPDATE fournisseurs SET statut='0' WHERE matricule=%s"
    cursor.execute(sql, (matricule,))

    conn.commit()
    cursor.close()
    conn.close()



# 6. Activer un fournisseur
def activer_fournisseur(matricule):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "UPDATE fournisseurs SET statut='1' WHERE matricule=%s"
    cursor.execute(sql, (matricule,))

    conn.commit()
    cursor.close()
    conn.close()



# 7. Lister tous les fournisseurs
def lister_fournisseurs():
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        SELECT id_fournisseurs, matricule, nom, adresse, mobile, email, statut
        FROM fournisseurs
    """

    cursor.execute(sql)
    rows = cursor.fetchall()

    table = PrettyTable([
        "ID", "Matricule", "Nom", "Adresse", "Mobile", "Email", "Statut"
    ])

    for row in rows:
        table.add_row(row)

    cursor.close()
    conn.close()

    return table

def id_fournisseurs_existe(id_four):
    conn = get_connection()
    cur = conn.cursor()

    sql = "SELECT COUNT(*) FROM fournisseurs WHERE id_fournisseurs = %s"
    cur.execute(sql, (id_four,))
    existe = cur.fetchone()[0] > 0

    cur.close()
    conn.close()
    return existe

# 8 get_fournisseur_by_matricule

def get_fournisseur_by_matricule(matricule):
    """
    Récupère un fournisseur unique par son matricule.
    Retourne un dictionnaire avec les colonnes ou None si introuvable.
    """
    conn = get_connection()
    cur = conn.cursor(dictionary=True)  # important pour obtenir un dict

    sql = "SELECT * FROM fournisseurs WHERE matricule=%s"
    cur.execute(sql, (matricule,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return None
    return row

