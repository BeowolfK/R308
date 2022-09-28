class Forme():
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__nom = ""

    @property
    def x(self):
        return self.__x

    @x.setter  
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter  
    def y(self, y):
        self.__y = y

    @property
    def nom(self):
        return self.__nom

    @nom.setter  
    def nom(self, nom):
        self.__nom = nom

    def affiche(self):
        print(f"X = {self.__x}, Y = {self.__y}, nom = {self.__nom}")

    def aire(self):
        pass

    def perimetre(self):
        pass