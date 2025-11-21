#création de la classe Fournisseur et ses différentes méthodes. 
class Fournisseur:
    def __init__(self, matricule=None, nom=None, adresse=None, mobile=None, email=None, statut="1", id_fournisseurs=None):
        self.id_fournisseurs = id_fournisseurs
        self.matricule = matricule
        self.nom = nom
        self.adresse = adresse
        self.mobile = mobile
        self.email = email
        self.statut = statut

    def __str__(self):
        return f"{self.matricule} - {self.nom} - {self.mobile} - ({self.statut})"

    def activer(self):
        self.statut = "1"

    def desactiver(self):
        self.statut = "0"
   