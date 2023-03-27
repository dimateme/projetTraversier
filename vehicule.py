
from decimal import *
from type import Type
from decimal import Decimal
# Création de la classe Vehicule
# Composition de la classe Vehicule
class Vehicule:
    def __init__(self, noIdentification:int, marque:str, modele:str, couleur:str, annee:int, immatriculation:str, nom:str, nombreRoue:bytes, prixTraverse:Decimal):
        # initialise les attributs de la classe Vehicule
        self.noIdentification = noIdentification
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.annee = annee
        self.immatriculation = immatriculation
        self.nom = nom
        self.nombreRoue = nombreRoue
        self.prixTraverse = prixTraverse

    def __str__(self):
        return f"{self.noIdentification} {self.marque} {self.modele} {self.couleur} {self.annee} {self.immatriculation} {self.nom} {self.nombreRoue} {self.prixTraverse}"
# création de la méthode GetHashCode qui permet de retourner le code de hachage de l'objet

    def __hash__(self):
        return hash(self.noIdentification + self.immatriculation)
    # création de la méthode Equals qui compare les vehicules par leur numéro d'identification
    def __eq__(self, other):
        if isinstance(other, Vehicule):
            return self.noIdentification == other.noIdentification and self.immatriculation == other.immatriculation
        return False