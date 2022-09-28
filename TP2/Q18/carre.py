from forme import Forme

class Carre(Forme):
    def __init__(self):
        self.__largeur = 0

    @property
    def largeur(self):
        return self.__largeur

    @largeur.setter  
    def largeur(self, largeur):
        self.__largeur = largeur

    def aire(self):
        return self.__largeur ** 2

    def perimetre(self):
        return self.__largeur * 4