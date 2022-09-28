class Rectangle():
    def __init__(self):
        self.__longueur
        self.__largeur

    @classmethod
    def get_data_input(self):
        self.__longueur = eval(input("Entrez la longueur: "))
        self.__largeur = eval(input("Entrez la largeur: ")) 
        
    @property
    def longueur(self):
        return self.__longueur

    @longueur.setter  
    def longueur(self, longueur):
        self.__longueur = longueur

    @property
    def largeur(self):
        return self.__largeur
        
    @largeur.setter
    def largeur(self, largeur):
        self.__largeur = largeur


class Parallepipede(Rectangle):
    def __init__(self):
        self.__hauteur = 0

    @classmethod
    def get_data_input(self):
        super().get_data_input()
        self.__hauteur = eval(input("Entrez la hauteur: "))

    @property
    def hauteur(self):
        return self.__hauteur

    @hauteur.setter
    def hauteur(self, hauteur):
        self.__hauteur = hauteur
        
    def Volume(self):
        return self.__hauteur * super().largeur * super().longueur

    def Affiche(self):
        print(f"Les attributs sont : longueur = {super().longueur}, largeur = {super().largeur}, hauteur = {self.__hauteur}")


