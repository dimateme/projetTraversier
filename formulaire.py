import sys
from datetime import datetime
import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
from PyQt5 import uic

from Traversier import Traversier
from client import Client
from employe import Employe
from xml.etree import ElementTree as ET

class Formulaire(QtWidgets.QMainWindow):

    # methode pour effacer les champs de l'employe
    def effacerChampsEmploye(self):
        self.edtNomEmp.clear()
        self.edtAdresseEmploye.clear()
        self.edtVilleEmploye.clear()
        self.edtProvinceEmploye.clear()
        self.edtCodePostalEmploye.clear()
        self.edtTelephoneEmploye.clear()
        self.edtCourrielEmploye.clear()
        self.edtNoEmploye.clear()
        self.edtNasEmploye.clear()

    # methode pour effacer les champs du traversier
    def effacerChampsTraversier(self):
        self.edtNomTraversier.clear()
        self.edtCapacitePersonne.clear()
        self.edtCapaciteVehicule.clear()

    # methode pour effacer les champs du d'un client
    def effacerChampsClient(self):
        self.edtNomClient.clear()
        self.edtAdresseClient.clear()
        self.edtVilleClient.clear()
        self.edtProvinceClient.clear()
        self.edtCodePostalClient.clear()
        self.edtTelephoneClient.clear()
        self.edtCourrielClient.clear()
        self.edtNoIdentificationClient.clear()


    def etatFormulaireVehicule(self):
        self.edtType.setEnabled(False)
        self.edtNombreRoues.setEnabled(False)
        self.edtMarque.setEnabled(False)
        self.edtModele.setEnabled(False)
        self.edtAnnee.setEnabled(False)
        self.edtCouleur.setEnabled(False)
        self.edtNoIdentification.setEnabled(False)
        self.edtImmatriculation.setEnabled(False)
        self.edtPrixTraverse.setEnabled(False)
        self.btnAjouterVehicule.setEnabled(False)

    def __init__(self):
        super(Formulaire, self).__init__()
        uic.loadUi("formulaire.ui", self)
        self.setFixedWidth(1500)
        self.setFixedHeight(900)
        self.btnAjouterEmploye.clicked.connect(self.ajouterEmploye)
        self.btnAjouterTraversier.clicked.connect(self.ajouterTraversier)
        self.btnAjouterClient.clicked.connect(self.ajouterClient)
        self.asVehicule.stateChanged.connect(self.afficherFormulaireVehicule)
        self.btnAjouterVehicule.clicked.connect(self.ajouterVehicule)
        self.etatFormulaireVehicule()
        self.show()

        self.employes = []
        # methode qui permet d'enregistrer les informations d'un employe dans un fichier xml


        # methode qui permet d'ajouter un un traversier
    def ajouterTraversier(self):
        nomTraversier = self.edtNomTraversier.text()
        capaciteVehicule = self.edtCapaciteVehicule.text()
        capacitePersonne = self.edtCapacitePersonne.text()
        anneeFabrication = self.dateFabrication.text()
        dateMiseService = self.dateMiseService.text()

        self.traversier = Traversier(nomTraversier, capaciteVehicule, capacitePersonne, anneeFabrication, dateMiseService)
        self.effacerChampsTraversier()


    # methode qui permet d'ajouter un client
    def ajouterClient(self):
        nomClient = self.edtNomClient.text()
        adresseClient = self.edtAdresseClient.text()
        villeClient = self.edtVilleClient.text()
        codePostalClient = self.edtCodePostalClient.text()
        provinceClient = self.edtProvinceClient.text()
        telephoneClient = self.edtTelephoneClient.text()
        courrielClient = self.edtCourrielClient.text()
        noIdentificationClient = self.edtNoIdentificationClient.text()
        if self.rdbHomme.isChecked():
            sexeClient = "M"
        else:
            sexeClient = "F"
        dateNaissanceClient = self.dateNaissance.text()

        self.client = Client(nomClient, adresseClient, villeClient, codePostalClient, provinceClient, telephoneClient, courrielClient, noIdentificationClient, sexeClient, dateNaissanceClient)
        self.listClient.addItem(str(self.client.nom) + " " + str(self.client.noIdentification))
        self.effacerChampsClient()


       # methode qui permet d'ajouter un vehicule
    def ajouterVehicule(self):
        typeVehicule = self.edtType.text()
        nombreRoues = self.edtNombreRoues.text()
        marque = self.edtMarque.text()
        modele = self.edtModele.text()
        annee = self.edtAnnee.text()
        couleur = self.edtCouleur.text()
        noIdentification = self.edtNoIdentification.text()
        immatriculation = self.edtImmatriculation.text()
        prixTraverse = self.edtPrixTraverse.text()





    def enregistrerXml(self, employes, fichier_xml):
        roote = ET.Element("Traverse")

        # ajouter un traversier dans le fichier xml
        traversier_xml = ET.SubElement(roote, "traversier")
        nomTraversier = ET.SubElement(traversier_xml, "nom")
        nomTraversier.text = self.traversier.nom
        capaciteVehicule = ET.SubElement(traversier_xml, "capaciteVehicule")
        capaciteVehicule.text = self.traversier.capaciteVehicule
        capacitePersonne = ET.SubElement(traversier_xml, "capacitePersonne")
        capacitePersonne.text = self.traversier.capacitePersonne
        anneeFabrication = ET.SubElement(traversier_xml, "anneeFabrication")
        anneeFabrication.text = self.traversier.anneeFabrication
        dateMiseService = ET.SubElement(traversier_xml, "dateMiseService")
        dateMiseService.text = self.traversier.dateMiseService

        # Parcourir la liste des employes et ajouter chaque employe dans le fichier xml
        for employe in employes:
            employe_xml = ET.SubElement(roote, "employe")
            employe_xml.set("noEmploye", str(employe.noEmploye))

            nom = ET.SubElement(employe_xml, "nom")
            nom.text = employe.nom

            adresse = ET.SubElement(employe_xml, "adresse")
            adresse.text = employe.adresse

            ville = ET.SubElement(employe_xml, "ville")
            ville.text = employe.ville

            province = ET.SubElement(employe_xml, "province")
            province.text = employe.province

            codePostal = ET.SubElement(employe_xml, "codePostal")
            codePostal.text = employe.codePostal

            telephone = ET.SubElement(employe_xml, "telephone")
            telephone.text = employe.telephone

            courriel = ET.SubElement(employe_xml, "courriel")
            courriel.text = employe.courriel

            noEmploye = ET.SubElement(employe_xml, "noEmploye")
            noEmploye.text = employe.noEmploye

            nAS = ET.SubElement(employe_xml, "nAS")
            nAS.text = employe.nAS

            dateEmbauche = ET.SubElement(employe_xml, "dateEmbauche")
            dateEmbauche.text = employe.dateEmbauche

            dateArret = ET.SubElement(employe_xml, "dateArret")
            dateArret.text = employe.dateArret

            tree = ET.ElementTree(roote)
            ET.indent(roote, space="    ")
            # tree.write(fichier_xml, encoding='utf-8', xml_declaration=True)
            with open(fichier_xml, "wb") as f:
                tree.write(f, encoding='utf-8', xml_declaration=True)
    def ajouterEmploye(self):

        nom = self.edtNomEmp.text()
        adresse = self.edtAdresseEmploye.text()
        ville = self.edtVilleEmploye.text()
        province = self.edtProvinceEmploye.text()
        codePostal = self.edtCodePostalEmploye.text()
        telephone = self.edtTelephoneEmploye.text()
        courriel = self.edtCourrielEmploye.text()
        noEmploye = self.edtNoEmploye.text()
        nAS = self.edtNasEmploye.text()
        dateEmbauche = self.dateEmbauche.text()
        dateArret = self.dateArret.text()
        self.employe = Employe(nom, adresse, ville, province, codePostal, telephone, courriel, noEmploye, nAS, dateEmbauche, dateArret)
        if self.employe not in self.traversier.listEmploye:
            self.traversier.listEmploye.append(self.employe)
            self.employes.append(self.employe)
            self.listEmployeTraversier.addItem(str(self.employe.noEmploye) + "-" + str(self.employe.nom))
            self.listEmploye.addItem(str(self.employe.noEmploye) + "-" + str(self.employe.nom))
            self.enregistrerXml(self.employes, "TransStLaurent.xml")
            self.effacerChampsEmploye()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Employe existe deja")
            msg.setWindowTitle("Informations")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()


    def afficherFormulaireVehicule(self):
        if self.asVehicule.isChecked():
            self.edtType.setEnabled(True)
            self.edtNombreRoues.setEnabled(True)
            self.edtMarque.setEnabled(True)
            self.edtModele.setEnabled(True)
            self.edtAnnee.setEnabled(True)
            self.edtCouleur.setEnabled(True)
            self.edtNoIdentification.setEnabled(True)
            self.edtImmatriculation.setEnabled(True)
            self.edtPrixTraverse.setEnabled(True)
            self.btnAjouterVehicule.setEnabled(True)

        else:
            self.edtType.setEnabled(False)
            self.edtNombreRoues.setEnabled(False)
            self.edtMarque.setEnabled(False)
            self.edtModele.setEnabled(False)
            self.edtAnnee.setEnabled(False)
            self.edtCouleur.setEnabled(False)
            self.edtNoIdentification.setEnabled(False)
            self.edtImmatriculation.setEnabled(False)
            self.edtPrixTraverse.setEnabled(False)
            self.btnAjouterVehicule.setEnabled(False)





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Formulaire()
    window.show()
    app.exec_()