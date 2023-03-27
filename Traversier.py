# Création de la classe traversier
from employe import Employe
from datetime import datetime
class Traversier:

        def __init__(self, nom:str, capaciteVehicule:int, capacitePersonne:int, anneeFabrication:datetime, dateMiseService:datetime):
        # initialise les attributs de la classe Traversier
            self.nom = nom
            self.capaciteVehicule = capaciteVehicule
            self.capacitePersonne = capacitePersonne
            self.anneeFabrication = anneeFabrication
            self.dateMiseService = dateMiseService
            self.listEmploye = []


        # Gestions des employés

        #Méthode qui permet d'obtenir la liste de tous les employés
        def ObtenirListeEmploye(self):
            return self.listEmploye
        #Méthode qui permet d'obtenir les informations d'un employé
        def ObtenirEmploye(self, employe: Employe):
            for self.employe in self.listEmploye:
                if employe.Equals(employe):
                    return employe
            return None



        #Méthode qui peremet de vérifier si un employé est présent avant de l'ajouter a la liste
        def AjouterEmploye(self, employe: Employe):
           self.listEmploye.append(employe)


        #Méthode qui permet de vérifier si un employé est présent avant de le supprimer de la liste
        def SupprimerEmploye(self, employe: Employe):
            employe_supprime = self.rechercherEmploye(employe.nAS)
            if employe_supprime:
                self.listEmploye.remove(employe)
                return True
            return False

       #Méthode qui permet de rechercher un employé dans la liste
        def rechercherEmploye(self, naS: int):
            for employe in self.listEmploye:
                if employe.nAS == naS:
                    return True
            return False
       #Méthode qui permet d'obtenir le nombre total d'employés dans la liste
        def ObtenirNombreEmploye(self):
            return len(self.listEmploye)
        #Méthode qui permet de determiner si la liste est vide
        def SiListeVide(self):
            return len(self.listEmploye) == 0

        # méthodes toString
        def __str__(self):
            return f"{self.nom} {self.capaciteVehicule} {self.capacitePersonne} {self.anneeFabrication} {self.dateMiseService}"
        #Méthode GetHashCode
        def GetHashCode(self):
            return hash(len(self.nom) + self.capaciteVehicule + self.capacitePersonne)
        #Méthode Equals
        def Equals(self, other):
            if isinstance(other, Traversier):
                return self.nom == other.nom
            return False



