"""
@author: meylan
Question 3 TP1
"""

class Rectangle:

    def __init__(self, longueur = 0, largeur = 0):
        self.__longueur = longueur
        self.__largeur = largeur
    
    @property
    def longueur(self):
        return self.__longueur

    @longueur.setter
    def longueur(self, longueur):
        self.__longueur = longueur

    @property
    def largeur(self):
        return self.__largeur

    @largeur.setter
    def largeur(self, largeur):
        self.__largeur = largeur

    @property
    def __perimetre(self):
        return (self.__longueur + self.__largeur)*2
    
    @property
    def __surface(self):
        return (self.__longueur * self.__largeur)
    
    @classmethod
    def get_Data_Input(self):
        longueur = eval(input("longueur : "))
        largeur = eval(input("largeur : "))
        return self(longueur, largeur)
        

    def affiche(self):
        print(f"Les attributs de la classe Rectangle sont : longueur = {self.__longueur}, largeur = {self.__largeur}")
        print(f"Périmetre {r.__perimetre}")
        print(f"Surface {r.__surface}")

r = Rectangle.get_Data_Input()
r.affiche()

