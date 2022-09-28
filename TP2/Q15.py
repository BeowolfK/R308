class Personne:
    def __init__(self, *args):
        self.__nom
        self.__prenom
        self.__age

    def set_Nom(self, nom):
        assert isinstance(nom, str)
        self.__nom = nom

    def set_Prenom(self, prenom):
        assert isinstance(prenom, str)
        self.__prenom = prenom

    def set_Age(self, age):
        assert isinstance(age, int)
        self.__age = age

    def get_Nom(self):
        return self.__nom

    def get_Prenom(self):
        return self.__prenom
    
    def get_Age(self):
        return self.__age

    def Affiche(self):
        return [self.__nom, self.__prenom, self.__age]