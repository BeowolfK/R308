from forme import Forme
from carre import Carre
from rectangle import Rectangle
from cercle import Cercle
from ellipse import Ellipse
from triangle import Triangle

f = Forme()
print("Ajouter les données pour la forme:")
f.x = int(input("X : "))
f.y = int(input("Y : "))
f.nom = input("nom : ")
f.affiche()

c = Carre()
print("Ajouter les données pour le carré:")
c.x = int(input("X : "))
c.y = int(input("Y : "))
c.nom = input("nom : ")
c.largeur = int(input("largeur : "))
print(f"Aire :{c.aire()}\nPerimetre :{c.perimetre()}")

r = Rectangle()
print("Ajouter les données pour le rectangle:")
r.x = int(input("X : "))
r.y = int(input("Y : "))
r.nom = input("nom : ")
r.largeur = int(input("largeur : "))
print(r.largeur)
r.longueur = int(input("longueur : "))
print(f"Aire :{r.aire()}\nPerimetre :{r.perimetre()}")

c2 = Cercle()
print("Ajouter les données pour le cercle:")
c2.x = int(input("X : "))
c2.y = int(input("Y : "))
c2.nom = input("nom : ")
c2.rayon = int(input("rayon : "))
print(f"Aire :{c2.aire()}\nPerimetre :{c2.perimetre()}")

e = Ellipse()
print("Ajouter les données pour le ellipse:")
e.x = int(input("X : "))
e.y = int(input("Y : "))
e.nom = input("nom : ")
e.r1 = int(input("rayon 1 : "))
e.r2 = int(input("rayon 2 : "))
print(f"Aire :{e.aire()}\nPerimetre :{e.perimetre()}")

t = Triangle()
print("Ajouter les données pour le triangle:")
t.x = int(input("X : "))
t.y = int(input("Y : "))
t.nom = input("nom : ")
t.longueur = int(input("longueur : "))
t.largeur = int(input("largeur : "))
if t.a <= 0 or t.b <= 0 or t.c <= 0:
    print("Triangle impossible")
else:
    print("Le triangle existe")
    print(f"Hauteur : {t.hauteur()} Aire : {t.aire()} Perimetre : {t.perimetre()}")