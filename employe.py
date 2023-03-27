# création de la classe heritière Employe
from personne import Personne
from datetime import datetime
class Employe(Personne):

    def __init__(self, nom, adresse, ville, province, codePostal, telephone, courriel, noEmploye:int, nAS:int, dateEmbauche:datetime, dateArret:datetime):
        """initialise les attributs de la classe Employe"""
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.noEmploye = noEmploye
        self.nAS = nAS
        self.dateEmbauche = dateEmbauche
        self.dateArret = dateArret



    def __str__(self):
        return f"{self.noEmploye} {self.nom} {self.adresse} {self.ville} {self.province} {self.codePostal} {self.telephone} {self.courriel} {self.nAS} {self.dateEmbauche} {self.dateArret}"

    def __eq__(self, other):
        return self.noEmploye == other.noEmploye and self.nAS == other.nAS

    def __hash__(self):
        return hash((self.noEmploye, self.nAS))

