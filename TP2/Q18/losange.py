from carre import Carre

class Losange(Carre):
    def __init__(self):
        self.__longueur

    @property
    def longueur(self):
        return self.__longueur
    
    @longueur.setter  
    def longueur(self, longueur):
        self.__longueur = longueur

    def aire(self):
        return (super().largeur * self.__longueur) / 2

    def perimetre(self):
        return super().largeur * 2 + self.__longueur * 2