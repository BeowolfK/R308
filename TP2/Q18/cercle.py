import math
from forme import Forme

class Cercle(Forme):
    def __init__(self):
        self.__rayon = 0

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter  
    def rayon(self, rayon):
        self.__rayon = rayon

    def aire(self):
        return round(math.pi * (self.__rayon ** 2), 2)

    def perimetre(self):
        return round(math.pi * self.__rayon * 2, 2)