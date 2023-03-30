# create a class Type
from decimal import Decimal
class Type:
    def __init__(self, nom:str, nombreRoue:bytes, prixTraverse:Decimal):
        # initialise les attributs de la classe Type
        self.nom = nom
        self.nombreRoue = nombreRoue
        self.prixTraverse = prixTraverse


    def __str__(self):
        return f"{self.nom} {self.nombreRoue} {self.prixTraverse}"

    def __eq__(self, other):
        return self.nom == other.nom
    def __hash__(self):
        return hash(len(self.nom)+self.nombreRoue)

