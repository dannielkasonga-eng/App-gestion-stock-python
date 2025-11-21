#création de la classe sortie et ses différentes méthodes.

class Sortie:
    def __init__(self, id_sorties=None, id_employes=None, date_sortie=None, destinataire= "particulier", statut=None, observation=None):
        self.id_sorties = id_sorties
        self.id_employes = id_employes
        self.date_sortie = date_sortie
        self.destinataire = destinataire
        self.statut = statut
        self.observation = observation
    def __str__(self):
        return f"{self.id_sorties} - {self.id_employes} - {self.date_sortie} - {self.destinataire}"
    
    