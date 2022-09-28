import math
from rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self):
        self.__a = super().longueur
        self.__b = super().largeur

    def perimetre(self):
        return self.__a + self.__b + self.__c

    def hauteur(self):
        s = (self.__a + self.__b + self.__c)/2
        heron = math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))
        self.__hauteur = (2 / self.__a) * heron
        return self.__hauteur
    
    def aire(self):
        return self.__a * self.__hauteur / 2
