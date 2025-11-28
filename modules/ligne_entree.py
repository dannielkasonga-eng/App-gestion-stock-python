#création de la classe LigneEntree et ses différentes méthodes.
class LigneEntree:
    def __init__(self, id_entrees=None, id_produits=None, numero_lot=None, peremption=None, quantite=None, prix_unitaire_entree=None, emplacement=None, id_ligne=None ):
        self.id_ligne = id_ligne
        self.id_entrees = id_entrees
        self.id_produits = id_produits
        self.numero_lot = numero_lot
        self.peremption = peremption
        self.quantite = quantite
        self.prix_unitaire_entree = prix_unitaire_entree
        self.emplacement = emplacement

    def __str__(self):
        return f"{self.id_entrees} - {self.id_produits} - {self.numero_lot} - {self.peremption} - {self.quantite} - {self.prix_unitaire_entree} - {self.emplacement}" 
