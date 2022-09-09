class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    @property
    def perimetre(self):
        return (self.longueur + self.largeur)*2
    
    @property
    def surface(self):
        return (self.longueur * self.largeur)
    
    def affiche(self):
        print(f"Les attributs de la classe Rectangle sont : longueur = {self.longueur}, largeur = {self.largeur}")
        print(f"Périmetre {r.perimetre}")
        print(f"Surface {r.surface}")

r = Rectangle(7, 5)
print(r)
r.affiche()

