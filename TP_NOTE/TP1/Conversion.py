"""
@author: Kénan Meylan TP1
Classe de conversion entre les devises euro, dollar et yuan 
Taux de conversion :
 - 1 yuan chinois = 0,14 euros
 - 1 dollar américain = 0,99 euros
 - 1 U.S. dollar = 6,96 yuan chinois
"""
class Devise():
    def __init__(self):
        self.__euro = 0
        self.__dollar = 0
        self.__yuan = 0
    
    @property
    def euro(self):
        return self.__euro

    @euro.setter
    def euro(self, euro):
        self.__euro = euro

    @property
    def dollar(self):
        return self.__dollar

    @dollar.setter
    def dollar(self, dollar):
        self.__dollar = dollar

    @property
    def yuan(self):
        return self.__yuan

    @yuan.setter
    def yuan(self, yuan):
        self.__yuan = yuan

    def deviseConvert(self, devise, value):
        if devise.upper() == "EU":
            self.__euro = value
            self.__dollar = round(value / 0.99, 2)
            self.__yuan = round(value / 0.14, 2)
        elif devise.upper() == "US":
            self.__dollar = value
            self.__euro = round(value * 0.99, 2)
            self.__yuan = round(value * 6.96, 2)
        elif devise.upper() == "YA":
            self.__yuan = value
            self.__euro = round(value * 0.14, 2)
            self.__dollar = round(value / 6.96, 2)
        else:
            exit(0)
