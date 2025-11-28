#création de la classe LigneSortie et ses différentes méthodes.
class LigneSortie:
    def __init__(self, id_sorties=None, id_produits=None, numero_lot=None, peremption=None, quantite=None, prix_unitaire_vente=None, id_ligne=None ):
        self.id_ligne = id_ligne
        self.id_sorties = id_sorties
        self.id_produits = id_produits
        self.numero_lot = numero_lot
        self.peremption = peremption
        self.quantite = quantite
        self.prix_unitaire_vente = prix_unitaire_vente
        

    def __str__(self):
        return f"{self.id_sorties} - {self.id_produits} - {self.numero_lot} - {self.peremption} - {self.quantite} - {self.prix_unitaire_vente}" 