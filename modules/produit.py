from Configuration.config import get_connection
from prettytable import PrettyTable

class Produit:
    def __init__(
        self,
        id_produits=None,
        ref_produit=None,      
        id_fournisseurs=None,
        code_atc=None,
        nom_commercial=None,
        dci=None,
        dosage=None,
        forme=None,
        conditionnement=None,
        stock_minimum=None,
        stock_maximum=None,
        description=None,
        statut="1"
    ):
        self.id_produits = id_produits       # utilisé pour état du stock
        self.ref_produit = ref_produit       # utilisé pour recherche/consultation/modification/desactivation/activation
        self.id_fournisseurs = id_fournisseurs
        self.code_atc = code_atc
        self.nom_commercial = nom_commercial
        self.dci = dci
        self.dosage = dosage
        self.forme = forme
        self.conditionnement = conditionnement
        self.stock_minimum = stock_minimum
        self.stock_maximum = stock_maximum
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.ref_produit} - {self.nom_commercial} - {self.stock_minimum} - {self.stock_maximum} - ({self.statut})"

    def activer(self):
        self.statut = "1"

    def desactiver(self):
        self.statut = "0"

    def etat_stock(self):
        """
        Vérifie l'état du stock du produit selon id_produits.
        """
        if not self.id_produits:
            raise ValueError("L'identifiant du produit (id_produits) doit être fourni pour vérifier le stock.")

        conn = get_connection()
        cursor = conn.cursor()

        table = PrettyTable([
            "ID", "Nom", "Stock initial", "Total entrées",
            "Total sorties", "Stock dispo", "Seuil", "État"
        ])

        # Infos principales
        sql_prod = """
            SELECT nom_commercial, stock_minimum, stock_maximum
            FROM produits
            WHERE id_produits = %s
        """
        cursor.execute(sql_prod, (self.id_produits,))
        row = cursor.fetchone()

        if not row:
            cursor.close()
            conn.close()
            return table  # produit inexistant

        nom, seuil_min, stock_initial = row

        # Total entrées
        sql_entrees = "SELECT COALESCE(SUM(quantite),0) FROM ligne_entree WHERE id_produits=%s"
        cursor.execute(sql_entrees, (self.id_produits,))
        total_entrees = cursor.fetchone()[0]

        # Total sorties
        sql_sorties = "SELECT COALESCE(SUM(quantite),0) FROM ligne_sortie WHERE id_produits=%s"
        cursor.execute(sql_sorties, (self.id_produits,))
        total_sorties = cursor.fetchone()[0]

        stock_disponible = (stock_initial + total_entrees) - total_sorties

        if stock_disponible <= 0:
            etat = "RUPTURE"
        elif stock_disponible <= seuil_min:
            etat = "ALERTE"
        else:
            etat = "OK"

        table.add_row([
            self.id_produits, nom, stock_initial,
            total_entrees, total_sorties, stock_disponible,
            seuil_min, etat
        ])

        cursor.close()
        conn.close()
        return table
