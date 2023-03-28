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





     # methode pour ajouter un vehicule à la liste des vehicules
    def ajouterVehicule(self, vehicule):
        self.listeVehicule.append(vehicule)
    # methode qui permet d#obtenir la liste des vehicules
    def obtenirListeVehicule(self):
        return self.listeVehicule
    # methode qui permet d#obtenir un vehicule
    def obtenirVehicule(self, vehicule):
        for self.vehicule in self.listeVehicule:
            if vehicule.Equals(vehicule):
                return vehicule
        return None
    # methode qui permet de supprimer un vehicule de la liste
    def supprimerVehicule(self, vehicule):
        vehicule_supprime = self.rechercherVehicule(vehicule.noVehicule)
        if vehicule_supprime:
            self.listeVehicule.remove(vehicule)
            return True
        return False
    # methode qui permet de rechercher un vehicule dans la liste
    def rechercherVehicule(self, noVehicule: int):
        for vehicule in self.listeVehicule:
            if vehicule.noVehicule == noVehicule:
                return True
        return False
    # methode qui permet d#obtenir le nombre total de vehicules dans la liste
    def obtenirNombreVehicule(self):
        return len(self.listeVehicule)
    # methode qui permet de determiner si la liste est vide
    def siListeVide(self):
        return len(self.listeVehicule) == 0


    # methode qui permet d'obtenir la liste des clients
    def obtenirListeClient(self):
        return self.listeClient
    # methode qui permet d'obtenir un client
    def obtenirClient(self, client):
        for self.client in self.listeClient:
            if client.Equals(client):
                return client
        return None
    # methode qui permet d'ajouter un client à la liste des clients
    def ajouterClient(self, client):
        self.listeClient.append(client)
    # methode qui permet de supprimer un client de la liste
    def supprimerClient(self, client):
        client_supprime = self.rechercherClient(client.noClient)
        if client_supprime:
            self.listeClient.remove(client)
            return True
        return False
    # methode qui permet de rechercher un client dans la liste
    def rechercherClient(self, noClient: int):
        for client in self.listeClient:
            if client.noClient == noClient:
                return True
        return False
    # methode qui permet d'obtenir le nombre total de clients dans la liste
    def obtenirNombreClient(self):
        return len(self.listeClient)
    # methode qui permet de determiner si la liste est vide
    def siListeClientVide(self):
        return len(self.listeClient) == 0

    # methode qui permet d'obtenir le nombre total de vehicules et de clients dans la liste
    def obtenirNombreTotal(self):
        return len(self.listeVehicule) + len(self.listeClient)

    def __str__(self):
        return f"{self.noTraverse} {self.dateHeure} {self.villeDepart} {self.employeInscription}"

    def __eq__(self, other):
        return self.noTraverse == other.noTraverse
    def __hash__(self):
        return hash((self.noTraverse))

