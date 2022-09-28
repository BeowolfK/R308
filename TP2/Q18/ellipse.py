import math
from cercle import Cercle

class Ellipse(Cercle):
    def __init__(self):
        self.__r1 = 0
        self.__r2 = 0

    @property
    def r1(self):
        return self.__r1

    @r1.setter  
    def r1(self, r1):
        self.__r1 = r1

    @property
    def r2(self):
        return self.__r2

    @r2.setter  
    def r2(self, r2):
        self.__r2 = r2
        
    def aire(self):
        return round(math.pi * self.__r1 * self.__r2, 2)

    def perimetre(self):
        return round(2 * math.pi * math.sqrt(0.5 * (self.__r1 + self.__r2)), 2)