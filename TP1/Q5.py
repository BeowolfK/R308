"""
@author: meylan
Question 5 TP1
"""

class Voiture:
    def __init__(self, marque ="", modele ="", volumeCarburant = 0, distanceParcouru = 0):
        self.marque = marque
        self.modele = modele
        self.volumeCarburant = volumeCarburant
        self.distanceParcouru = distanceParcouru
    
    def get_Data(self, marque, modele, volumeCarburant, distanceParcouru):
        self.marque = marque
        self.modele = modele
        self.volumeCarburant = volumeCarburant
        self.distanceParcouru = distanceParcouru

    def consommation(self):
        coefKmEur = ((100*100)/self.distanceParcouru)/100
        consoEur = coefKmEur * self.volumeCarburant

        consoUsa = (self.distanceParcouru /1.609) / (self.volumeCarburant / 3.785)
        print(self.marque, self.modele, self.distanceParcouru, f"({round(consoEur, 2)}, {round(consoUsa, 2)})")
v = Voiture()
v.get_Data(
    input("Marque = "),
    input("Modele = "),
    int(input("Volume Carburant = ")),
    int(input("Distance Parcouru = ")),
)
v.consommation()