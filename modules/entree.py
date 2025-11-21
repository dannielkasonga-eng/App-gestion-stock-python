#création de la classe Entree et ses différentes méthodes
class Entree:
    def __init__(self, id_entrees=None, id_fournisseurs=None, date_commande=None, statut_commande=None, date_reception=None, observation=None ):
        self.id_entrees = id_entrees
        self.id_fournisseurs = id_fournisseurs
        self.date_commande = date_commande
        self.statut_commande = statut_commande
        self.date_reception = date_reception
        self.observation = observation
    def __str__(self):
        return f"{self.id_entrees} - {self.id_fournisseurs} - {self.date_commande} - {self.statut_commande} - {self.date_reception}"    
    

