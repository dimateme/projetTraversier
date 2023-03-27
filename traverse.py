# Création de la classe traverse
from employe import Employe
from datetime import datetime
class Traverse:
    def __init__(self, noTraverse:int,dateHeure:datetime, villeDepart:str, employeInscription):
        """initialise les attributs de la classe Traverse"""
        self.noTraverse = noTraverse
        self.dateHeure = dateHeure
        self.villeDepart = villeDepart
        self.employeInscription = employeInscription
        self.listeVehicule = []
        self.listeClient = []


    def __str__(self):
        return f"{self.noTraverse} {self.dateHeure} {self.villeDepart} {self.employeInscription}"

    def __eq__(self, other):
        return self.noTraverse == other.noTraverse
    def __hash__(self):
        return hash((self.noTraverse))

