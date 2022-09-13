"""
@author: meylan
Question 8 TP2
execution
"""

from Q8 import CompteBancaire

num = input("num de compte : ")
nom = input("nom : ")
solde = eval(input("solde initial : "))

compte = CompteBancaire(num, nom, solde)

while True:
    code = ""
    while (code != "V" and code != "R" and code != "F"):
        code = input("Operation (V, R, F pour fin) : ").upper()
    if code == "F":
        break
    elif code == "V":
        montant = eval(input("versement de : "))
        compte.versement(montant)
    elif code == "R":
        montant = eval(input("retrait de : "))
        compte.retrait(montant)
    compte.afficher()