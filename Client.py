from Personne import Personne
class Client(Personne):
    def __init__(self, nom, prenom, ville, province, code_postal, telephone, courriel, numeroIdentification, sexe, dateNaissance):
        """initialise les attributs de la classe Client"""
        super().__init__(nom, prenom, ville, province, code_postal, telephone, courriel)
        self.numeroIdentification = numeroIdentification
        self.sexe = sexe
        self.dateNaissance = dateNaissance
# Setters
    def setNumeroIdentification(self, numeroIdentification):
        self.numeroIdentification = numeroIdentification
    def setSexe(self, sexe):
        self.sexe = sexe
    def setDateNaissance(self, dateNaissance):
        self.dateNaissance = dateNaissance
# Getters
    def getNumeroIdentification(self):
        return self.numeroIdentification
    def getSexe(self):
        return self.sexe
    def getDateNaissance(self):
        return self.dateNaissance
# création de la méthode ToString
    def __str__(self):
        return f"{self.numeroIdentification} {self.nom} {self.prenom} {self.ville} {self.province} {self.code_postal} {self.telephone} {self.courriel} {self.sexe} {self.dateNaissance}"
# création de la méthode GetHashCode
    def GetHashCode(self):
        return hash(self.numeroIdentification)
# création de la méthode Equals
    def Equals(self, other):
        if isinstance(other, Client):
            return self.numeroIdentification == other.numeroIdentification
        return False