#création de la classe employes et ses différentes méthodes.
class Employe:
    def __init__(self, matricule=None, nom=None, 
                 prenom=None, date_naissance=None, 
                 genre=None, adresse=None, 
                 mobile=None, email=None, fonction=None, 
                 statut="1", id_employes=None, 
                 date_creation=None):

        self.id_employes = id_employes
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.genre = genre
        self.adresse = adresse
        self.mobile = mobile
        self.email = email
        self.fonction = fonction
        self.date_creation = date_creation
        self.statut = statut

    def __str__(self):
        return f"{self.matricule} - {self.nom} - {self.prenom} - {self.fonction} - {self.mobile}"


    def activer(self):
        self.statut = "1"

    def desactiver(self):
        self.statut = "0"

    