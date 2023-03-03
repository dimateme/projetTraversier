# creér une classe Personne
class Personne:
    def __init__(self, nom, prenom, ville,  province, code_postal, telephone, courriel):
        """initialise les attributs de la classe Personne"""
        self.nom = nom
        self.prenom = prenom
        self.ville = ville
        self.province = province
        self.code_postal = code_postal
        self.telephone = telephone
        self.courriel = courriel

# setter
    def setNom(self, nom):
        self.nom = nom
    def setPrenom(self, prenom):
        self.prenom = prenom
    def setVille(self, ville):
        self.ville = ville
    def setProvince(self, province):
        self.province = province
    def setCodePostal(self, code_postal):
        self.code_postal = code_postal
    def setTelephone(self, telephone):
        self.telephone = telephone
    def setCourriel(self, courriel):
        self.courriel = courriel


# getter
    def getNom(self):
        return self.nom
    def getPrenom(self):
        return self.prenom
    def getVille(self):
        return self.ville
    def getProvince(self):
        return self.province
    def getCodePostal(self):
        return self.code_postal
    def getTelephone(self):
        return self.telephone
    def getCourriel(self):
        return self.courriel



