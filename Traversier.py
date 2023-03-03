# Création de la classe traversier
from Employe import Employe
class Traversier:
        def __init__(self, nom, capaciteVehicule, capacitePersonne, anneeFabrication, dateMiseService):
        # initialise les attributs de la classe Traversier
            self.nom = nom
            self.capaciteVehicule = capaciteVehicule
            self.capacitePersonne = capacitePersonne
            self.anneeFabrication = anneeFabrication
            self.dateMiseService = dateMiseService
            self.listEmploye = []# liste d'employé
