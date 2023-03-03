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
# Setters
def setNoEmploye(self, noEmploye):
    self.noEmploye = noEmploye
def setNAS(self, nAS):
    self.nAS = nAS
def setDateEmbauche(self, dateEmbauche):
    self.dateEmbauche = dateEmbauche
def setDateArret(self, dateArret):
    self.dateArret = dateArret

# Getters
def getNoEmploye(self):
    return self.noEmploye
def getNAS(self):
    return self.nAS
def getDateEmbauche(self):
    return self.dateEmbauche
def getDateArret(self):
    return self.dateArret

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