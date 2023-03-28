from personne import Personne
from datetime import datetime
class Client(Personne):
    def __init__(self, nom, adresse,ville, province, codePostal, telephone, courriel, numeroIdentification:int, sexe:str, dateNaissance:datetime):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.numeroIdentification = numeroIdentification
        self.sexe = sexe
        self.dateNaissance = dateNaissance

# création de la méthode ToString
    def __str__(self):
        return f"{self.numeroIdentification} {self.nom} {self.adresse} {self.ville} {self.province} {self.codePostal} {self.telephone} {self.courriel} {self.sexe} {self.dateNaissance}"
# création de la méthode GetHashCode
    def __eq__(self, other):
        return self.numeroIdentification == other.numeroIdentification

    def __hash__(self):
        return hash(self.numeroIdentification)