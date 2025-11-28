from Configuration.config import get_connection
from prettytable import PrettyTable

# 1 ajouter employé

def ajouter_employe(employe):
    """
    Ajoute un nouvel employé dans la base.
    employe = objet Employe déjà rempli
    """

    conn = get_connection()
    cur = conn.cursor()

    sql = """
        INSERT INTO employes(
            matricule, nom, prenom, date_naissance,
            genre, adresse, mobile, email, fonction,
            statut
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        employe.matricule,
        employe.nom,
        employe.prenom,
        employe.date_naissance,
        employe.genre,
        employe.adresse,
        employe.mobile,
        employe.email,
        employe.fonction,
        employe.statut,
    )

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()

# 2 modifier employé

def modifier_employe(matricule, employe):
    """
    Modifie un employé existant.
    matricule = matricule de l'employé cible
    employe = objet Employe avec les nouvelles valeurs
    """

    conn = get_connection()
    cur = conn.cursor()

    sql = """
        UPDATE employes SET
            matricule=%s,
            nom=%s, 
            prenom=%s, 
            date_naissance=%s,
            genre=%s, 
            adresse=%s, 
            mobile=%s,
            email=%s, 
            fonction=%s, 
            statut=%s
        WHERE matricule=%s
    """

    values = (
        employe.matricule,
        employe.nom,
        employe.prenom,
        employe.date_naissance,
        employe.genre,
        employe.adresse,
        employe.mobile,
        employe.email,
        employe.fonction,
        employe.statut,
        matricule
    )

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()

# 3 rechercher les employés (info restreintes)

def rechercher_employe(matricule):
    """
    Recherche un employé par son matricule.
    matricule : string de 10 caractères
    """
    conn = get_connection()
    cur = conn.cursor()

    table = PrettyTable(["Matricule", "Nom", "Prénom", "Naissance", "Genre", "Adresse", "Création"])

    sql = """
        SELECT matricule, nom, prenom, date_naissance, genre, adresse, date_creation
        FROM employes
        WHERE matricule=%s
    """

    cur.execute(sql, (matricule,))
    row = cur.fetchone()
    if row:
        table.add_row(row)

    cur.close()
    conn.close()
    return table

# 4 consulter les employés

def consulter_employe(matricule):
    """
    Consulte un employé et ses sorties.
    matricule : string de 10 caractères
    """
    conn = get_connection()
    cursor = conn.cursor()

    table = PrettyTable([
        "ID", "Matricule", "Nom", "Prenom", "Mobile", "Email",
        "Fonction", "Statut employe", 
        "ID sortie", "Date sortie", "Destinataire",
        "Statut sortie", "Observation"
    ])

    sql = """
        SELECT e.id_employes AS ID,
               e.matricule,
               e.nom,
               e.prenom,
               e.mobile,
               e.email,
               e.fonction,
               e.statut AS statut_employe,
               s.id_sorties AS sortie,
               s.date_sortie,
               s.destinataire,
               s.statut AS statut_sortie,
               s.observation
        FROM employes e
        LEFT JOIN gestion_sortie s
        ON e.id_employes = s.id_employes
        WHERE e.matricule = %s
    """

    cursor.execute(sql, (matricule,))
    rows = cursor.fetchall()
    for row in rows:
        table.add_row(row)

    cursor.close()
    conn.close()
    return table

# 5 désactiver employé

def desactiver_employe(matricule):
    """
    Met le statut d'un employé à 0 (inactif).
    """

    conn = get_connection()
    cur = conn.cursor()

    sql = "UPDATE employes SET statut=0 WHERE matricule=%s"

    cur.execute(sql, (matricule,))
    conn.commit()

    cur.close()
    conn.close()

# 6 activer employé

def activer_employe(matricule):
    """
    Met le statut d'un employé à 1 (actif).
    """

    conn = get_connection()
    cur = conn.cursor()

    sql = "UPDATE employes SET statut=1 WHERE matricule=%s"

    cur.execute(sql, (matricule,))
    conn.commit()

    cur.close()
    conn.close()

# 7 lister tous les employes

def lister_employes():
    """
    Affiche tous les employés enregistrés.
    """

    conn = get_connection()
    cur = conn.cursor()

    table = PrettyTable([
        "Matricule", "Nom", "Prénom", "Date Naissance",
        "Genre", "Adresse", "Mobile", "Email",
        "Fonction", "Statut"
    ])

    sql = "SELECT matricule, nom, prenom, date_naissance, genre, adresse, mobile, email, fonction, statut FROM employes"

    cur.execute(sql)

    for row in cur.fetchall():
        table.add_row(row)

    cur.close()
    conn.close()

    return table

# 8 get_employe_by_matricule

def get_employe_by_matricule(matricule):
    """
    Récupère un employé unique par son matricule.
    Retourne un dictionnaire avec les colonnes ou None si introuvable.
    """
    conn = get_connection()
    cur = conn.cursor(dictionary=True)  # important pour obtenir un dict

    sql = "SELECT * FROM employes WHERE matricule=%s"
    cur.execute(sql, (matricule,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return None
    return row
