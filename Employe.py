# création de la classe heritière Employe
from Personne import Personne
class Employe(Personne):
    def __init__(self, nom, prenom, ville, province, code_postal, telephone, courriel, noEmploye, nAS, dateEmbauche, dateArret):
        """initialise les attributs de la classe Employe"""
        super().__init__(nom, prenom, ville, province, code_postal, telephone, courriel)
        self.noEmploye = noEmploye
        self.nAS = nAS
        self.dateEmbauche = dateEmbauche
        self.dateArret = dateArret

"""Employe toString method"""
def __str__(self):
    return f"{self.noEmploye} {self.nom} {self.prenom} {self.ville} {self.province} {self.code_postal} {self.telephone} {self.courriel} {self.nAS} {self.dateEmbauche} {self.dateArret}"

# création de la méthode GetHashCode
def GetHashCode(self):
    return hash(self.nAS)
# création de la méthode Equals
def Equals(self, other):
    if isinstance(other, Employe):
        return self.nAS == other.nAS
    return False