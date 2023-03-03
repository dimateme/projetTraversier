# create a class Type
class Type:
    def __init__(self, nom, nombreRoue, prixTraverse):
        # initialise les attributs de la classe Type
        self.nom = nom
        self.nombreRoue = nombreRoue
        self.prixTraverse = prixTraverse
#setter
    def setNom(self, nom):
        self.nom = nom
    def setNombreRoue(self, nombreRoue):
        self.nombreRoue = nombreRoue
    def setPrixTraverse(self, prixTraverse):
        self.prixTraverse = prixTraverse
# getter
    def getNom(self):
        return self.nom
    def getNombreRoue(self):
        return self.nombreRoue
    def getPrixTraverse(self):
        return self.prixTraverse

    def __str__(self):
        return f"{self.nom} {self.nombreRoue} {self.prixTraverse}"

    def GetHashCode(self):
        return hash(self.nom, self.prixTraverse)
    def Equals(self, other):
        if isinstance(other, Type):
            return self.nom == other.nom
        return False