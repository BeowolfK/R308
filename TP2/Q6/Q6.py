"""
@author: meylan
Question 6 TP2
"""
class IMC:
    def __init__(self, nom, age, taille, poids):
        self.nom = nom
        self.age = age
        self.taille = taille
        self.poids = poids

    @classmethod
    def get_user_input(self):
        nom = int(input("nom : "))
        age = int(input("age : "))
        taille = float(input("taille : "))
        poids = float(input("poids : "))
        return self(nom, age, taille, poids)
    
    @property
    def imc(self):
        imc = self.poids / (self.taille**2)
        return imc
    
    @property
    def interpretation(self):
        imc = self.imc
        if imc < 16.5:
            return "denutrition"
        elif 16.5 <= imc < 18.5:
            return "maigreur"
        elif 18.5 <= imc < 25:
            return "corpulence normale"
        elif 25 <= imc < 30:
            return "surpoids"
        elif 30 <= imc < 35:
            return "obésité modérée"
        elif 35 <= imc < 40:
            return "obésité sévère"
        elif imc > 40:
            return "obésité morbide"
    
    def __str__(self):
        return f"Bonjour {self.nom}\nVotre IMC est exactement de {self.imc}\nVous etes en {self.interpretation}"

h = IMC("Hadji", 18, 1.70, 62)
print(h)
k = IMC("Kenan", 20, 1.69, 154)
print(k)
H = IMC("Hugo", 19, 1.95, 70)
print(H)
