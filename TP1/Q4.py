"""
@author: meylan
Question 4 TP1
"""

from math import pi, sqrt

class Cercle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r
    
    @property
    def surface(self):
        return pi * self.r ** 2
    
    @property
    def perimetre(self):
        return pi * self.r * 2
    
    def testAppartenance(self, x, y):
        distance = sqrt((x - self.a)**2 + (y - self.b)**2)
        if distance == self.r:
            return True
        return False

c = Cercle(int(input("x = ")), int(input("y = ")), int(input("r = ")))
print("Périmetre", c.perimetre)
print("Surface", c.surface)
print(c.testAppartenance(1, 1))