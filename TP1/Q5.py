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
        gallon = self.volumeCarburant * 3.785
        distance = self.distanceParcouru * 1.609
        print(distance / gallon)

v = Voiture()
v.get_Data(
    input("Marque = "),
    input("Modele = "),
    int(input("Volume Carburant = ")),
    int(input("Distance Parcouru = ")),
)
v.consommation()