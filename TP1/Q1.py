"""
@author: meylan
Question 1 TP1
"""
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def Affiche(self):
        print(f"Les attributs de la classe Rectangle sont : longueur = {self.longueur}, largeur = {self.largeur}")

    def __repr__(self):
        return f"Les attributs de la classe Rectangle sont : longueur = {self.longueur}, largeur = {self.largeur}"

r = Rectangle(9, 7)
print(r)
r.Affiche()


