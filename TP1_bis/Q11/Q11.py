"""
@author: meylan
Question 9 TP2
class
"""

from math import sqrt

class racine:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
    
    def get_data(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_delta(self):
        self.delta = (self.b**2)-4*self.a*self.c
        return self.delta
    
    def trait_delta(self):
        if self.delta<0:
            print("aucune solution")
        elif self.delta == 0:
            print(f"racine = {-self.b/(2*self.a)}")
        else:
            r1 = (-self.b-sqrt(self.delta))/(2*self.a)
            r2 = (-self.b+sqrt(self.delta))/(2*self.a)
            print(f"2racines : {round(r1, 2), round(r2, 2)}")
