"""
@author: meylan
Question 9 TP2
classe
"""

class CompteBancaire:
    def __init__(self, numeroCompte, nom, solde):
        self.__numeroCompte = numeroCompte
        self.__nom = nom
        self.__solde = solde
    
    @property
    def numeroCompte(self):
        return self.__numeroCompte

    @property
    def nom(self):
        return self.__nom

    @property
    def solde(self):
       return self.__solde

    @solde.setter
    def solde(self, solde):
        self.__solde = solde


    def versement(self, montant):
        self.__solde += montant
    
    def retrait(self, montant):
        if self.__solde - montant < 0:
            if self.__solde < 0:
                self.agios(montant)
            else:
                temp = montant - self.__solde
                self.__solde = 0
                self.agios(temp)
            
        else:
            self.__solde -= montant
    
    def agios(self, montant):
        self.__solde -= montant*1.05

    def afficher(self):
        print("numero : " + str(self.__numeroCompte))
        print("nom : " + self.__nom)
        print("solde : " + str(self.__solde))