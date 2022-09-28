"""
@author: meylan
Question 7 TP2
Classe
"""

class Temp:
    def __init__(self):
        self.__celsius = 0
        self.__farheneit = 0
    
    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, celsius):
        self.__celsius = int(celsius)
    
    @property
    def farheneit(self):
        return self.__farheneit

    @farheneit.setter
    def farheneit(self, farheneit):
        self.__farheneit = int(farheneit)

    def far(self):
        self.__celsius = (self.__farheneit-32)/1.8
    
    def cel(self):
        self.__farheneit = (self.__celsius*9/5)+32