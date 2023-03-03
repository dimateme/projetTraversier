from Type import Type
# Création de la classe Vehicule
# Composition de la classe Vehicule
class Vehicule:
    def __init__(self, noIdentification, marque, modele, couleur, annee, immatriculation, nom, nombreRoue, prixTraverse):
        # initialise les attributs de la classe Vehicule
        self.noIdentification = noIdentification
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.annee = annee
        self.immatriculation = immatriculation
        self.type = Type(nom, nombreRoue, prixTraverse)
# Setters
    def setNoIdentification(self, noIdentification):
        self.noIdentification = noIdentification
    def setMarque(self, marque):
        self.marque = marque
    def setModele(self, modele):
        self.modele = modele
    def setCouleur(self, couleur):
        self.couleur = couleur
    def setAnnee(self, annee):
        self.annee = annee
    def setImmatriculation(self, immatriculation):
        self.immatriculation = immatriculation
    def setType(self, nom, nombreRoue, prixTraverse):
        self.type = Type(nom, nombreRoue, prixTraverse)
# Getters
    def getNoIdentification(self):
        return self.noIdentification
    def getMarque(self):
        return self.marque
    def getModele(self):
        return self.modele
    def getCouleur(self):
        return self.couleur
    def getAnnee(self):
        return self.annee
    def getImmatriculation(self):
        return self.immatriculation
    def getType(self):
        return self.type

    def __str__(self):
        return f"{self.noIdentification} {self.marque} {self.modele} {self.couleur} {self.annee} {self.immatriculation} {self.type.nom} {self.type.nombreRoue} {self.type.prixTraverse}"
# création de la méthode GetHashCode qui permet de retourner le code de hachage de l'objet

    def GetHashCode(self):
        return hash(self.noIdentification)
    # création de la méthode Equals qui compare les vehicules par leur numéro d'identification
    def Equals(self, other):
        if isinstance(other, Vehicule):
            return self.noIdentification == other.noIdentification
        return False