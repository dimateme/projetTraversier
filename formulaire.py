import sys
from datetime import datetime
import datetime
from decimal import Decimal
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
from PyQt5 import uic

from traverse import Traverse
from traversier import Traversier
from client import Client
from employe import Employe
from xml.etree import ElementTree as ET

from type import Type
from vehicule import Vehicule


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

    # methode pour effacer les champs du d'un vehicule
    def effacerChampsVehicule(self):
        self.edtType.clear()
        self.edtNombreRoues.clear()
        self.edtMarque.clear()
        self.edtModele.clear()
        self.edtAnnee.clear()
        self.edtCouleur.clear()
        self.edtNoIdentification.clear()
        self.edtImmatriculation.clear()
        self.edtPrixTraverse.clear()


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
        self.btnAjouterTraverse.clicked.connect(self.ajouterTraverse)
        self.etatFormulaireVehicule()
        self.montantTransportParPesonne = 25
        self.edtPrixTraverse.setReadOnly(True)
        self.edtNombrePersonne.textChanged.connect(self.calculerMontantTransport)

        self.montantTotal: Decimal
        self.heure=QTime.currentTime()
        self.edtHeureTraverse.setTime(self.heure)
        self.clients = [] # liste des clients
        self.employes = []  # liste des employes
        self.nomTraversier = None # nom du traversier
        self.numeroTraverse = None # numero de traverse
        self.numeroTraverse = None # numero de traverse

        self.show()







    # methode qui permet de calculer le montant du traverse
    def calculerMontantTransport(self):
        self.nombrePersonne = self.edtNombrePersonne.text()
        if self.nombrePersonne == "":
            self.edtPrixTraverse.setText("")
        else:
            self.montantTotal =Decimal((self.montantTransportParPesonne) * int(self.nombrePersonne))
            self.edtPrixTraverse.setText(str(f"${self.montantTotal:.2f}"))



    # methode qui permet d'ajouter un un traversier
    def ajouterTraversier(self):
        nomTraversier = self.edtNomTraversier.text()
        capaciteVehicule = self.edtCapaciteVehicule.text()
        capacitePersonne = self.edtCapacitePersonne.text()
        anneeFabrication = self.dateFabrication.text()
        dateMiseService = self.dateMiseService.text()

        self.traversier = Traversier(nomTraversier, capaciteVehicule, capacitePersonne, anneeFabrication, dateMiseService)
        self.nomTraversier = self.traversier.nom

        self.effacerChampsTraversier()





    # methode qui permet d'ajouter un vehicule
    def ajouterVehicule(self):
        typeVehicule = self.edtType.text()
        nombreRoues = self.edtNombreRoues.text()
        marque = self.edtMarque.text()
        modele = self.edtModele.text()
        annee = self.edtAnnee.text()
        couleur = self.edtCouleur.text()
        # self.nombrePersonne = self.edtNombrePersonne.text()
        noIdentification = self.edtNoIdentification.text()
        immatriculation = self.edtImmatriculation.text()
        prixTraverse = Decimal(self.montantTotal)
        self.type=Type(typeVehicule, nombreRoues, prixTraverse)
        print(self.type.nom, self.type.nombreRoue, marque, modele, annee, couleur, noIdentification, immatriculation, prixTraverse)
        self.vehicule = Vehicule(self.type.nom, self.type.nombreRoue, marque, modele, annee, couleur, noIdentification, immatriculation, self.type.prixTraverse)
        self.listVehiculeTraverse.addItem(self.vehicule.nom + "-" + self.vehicule.modele + "-" + self.vehicule.marque)

        if self.numeroTraverse is not None:
            if self.vehicule not in self.traverse.listeVehicule:
                self.traverse.ajouterVehicule(self.vehicule)
                self.listVehiculeTraverse.addItem(self.vehicule.nom + "-" + self.vehicule.modele + "-" + self.vehicule.marque)
                self.effacerChampsVehicule()
                self.etatFormulaireVehicule()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Employe existe deja")
                msg.setWindowTitle("Informations")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Veuillez ajouter une traverse avant d'ajouter un vehicule")
            msg.setWindowTitle("Informations")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.effacerChampsVehicule()



        # un compteur pour le nombre de vehicule








    def enregistrerXml(self,fichier_xml):
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

        # pqrcourir la liste des clients et ajouter chaque client dans le fichier xml
        # for self.client in self.clients:
        #     client_xml = ET.SubElement(roote, "client")
        #     client_xml.set("noClient", str(self.client.noIdentificationClient))
        #
        #     nom = ET.SubElement(client_xml, "nom")
        #     nom.text = self.client.nom



        # Parcourir la liste des employes et ajouter chaque employe dans le fichier xml
        for self.employe in self.employes:
            employe_xml = ET.SubElement(roote, "employe")
            employe_xml.set("noEmploye", str(self.employe.noEmploye))

            nom = ET.SubElement(employe_xml, "nom")
            nom.text = self.employe.nom

            adresse = ET.SubElement(employe_xml, "adresse")
            adresse.text = self.employe.adresse

            ville = ET.SubElement(employe_xml, "ville")
            ville.text = self.employe.ville

            province = ET.SubElement(employe_xml, "province")
            province.text = self.employe.province

            codePostal = ET.SubElement(employe_xml, "codePostal")
            codePostal.text = self.employe.codePostal

            telephone = ET.SubElement(employe_xml, "telephone")
            telephone.text = self.employe.telephone

            courriel = ET.SubElement(employe_xml, "courriel")
            courriel.text = self.employe.courriel

            noEmploye = ET.SubElement(employe_xml, "noEmploye")
            noEmploye.text = self.employe.noEmploye

            nAS = ET.SubElement(employe_xml, "nAS")
            nAS.text = self.employe.nAS

            dateEmbauche = ET.SubElement(employe_xml, "dateEmbauche")
            dateEmbauche.text = self.employe.dateEmbauche

            dateArret = ET.SubElement(employe_xml, "dateArret")
            dateArret.text = self.employe.dateArret


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

        # si le traversier  n'existe pas
        if self.nomTraversier is not None:
            self.employe = Employe(nom, adresse, ville, province, codePostal, telephone, courriel, noEmploye, nAS,
                                   dateEmbauche, dateArret)
            if self.employe not in self.traversier.listEmploye:
                self.traversier.listEmploye.append(self.employe)
                self.employes.append(self.employe)
                self.listEmployeTraversier.addItem(str(self.employe.noEmploye) + "-" + str(self.employe.nom))
                self.listEmploye.addItem(str(self.employe.noEmploye) + "-" + str(self.employe.nom))
                self.cboEmployeJour.addItem(str(self.employe.nom))
                self.enregistrerXml("TransStLaurent.xml")
                self.effacerChampsEmploye()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Employe existe deja")
                msg.setWindowTitle("Informations")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("ajouter un traversier avant d'ajouter un employe")
            msg.setWindowTitle("Informations")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.effacerChampsEmploye()

    # methode qui permet de créer un traverse
    def ajouterTraverse(self):
            noTraverse = self.edtNumeroTraverse.text()
            villeDeDepart = self.edtVilleTraverse.text()
            heureTraverse = self.heure.toString("hh:mm")
            employeInscription = self.cboEmployeJour.currentText()
            print(noTraverse, heureTraverse, villeDeDepart, employeInscription)
            self.traverse = Traverse(noTraverse, heureTraverse, villeDeDepart, employeInscription)
            self.numeroTraverse = str(self.traverse.noTraverse)
            self.numeroTraverse = str(self.traverse.noTraverse)


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

            if self.numeroTraverse is not None:
                self.client = Client(nomClient, adresseClient, villeClient, codePostalClient, provinceClient, telephoneClient, courrielClient, noIdentificationClient, sexeClient, dateNaissanceClient)

                if self.client not in self.traverse.listeClient:
                    self.clients.append(self.client)
                    self.traverse.listeClient.append(self.client)
                    # self.enregistrerXml("TransStLaurent.xml")
                    self.effacerChampsClient()
                    # self.enregistrerXml("TransStLaurent.xml")
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Client existe deja")
                    msg.setWindowTitle("Informations")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    self.effacerChampsClient()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("ajouter un traverse")
                msg.setWindowTitle("Informations")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                self.effacerChampsClient()







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