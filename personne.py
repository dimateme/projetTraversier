# creér une classe Personne
class Personne:
    def __init__(self, nom :str, adresse:str, ville:str,  province:str, codePostal:str, telephone:str, courriel:str):
        """initialise les attributs de la classe Personne"""
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.codePostal = codePostal
        self.telephone = telephone
        self.courriel = courriel

