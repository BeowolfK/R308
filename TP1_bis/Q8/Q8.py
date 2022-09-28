"""
@author: meylan
Question 8 TP2
classe
"""

class CompteBancaire:
    def __init__(self, numeroCompte, nom, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde
    
    def versement(self, montant):
        self.solde += montant
    
    def retrait(self, montant):
        if self.solde - montant > 0:
            self.numeroCompte -= montant
        else:
            print("solde insuffisant")
    
    def afficher(self):
        print("numero : " + str(self.numeroCompte))
        print("nom : " + self.nom)
        print("solde : " + str(self.solde))