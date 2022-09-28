from Q14 import Parallepipede

while True:
  print("Création d'un nouveau parallepipede:")
  hauteur = eval(input("Entrez l'hauteur: "))
  longueur = eval(input("Entrez la longueur: "))
  largeur = eval(input("Entrez la largeur: "))
  
  p=Parallepipede()
  p.hauteur = hauteur
  p.longueur = longueur
  p.largeur = largeur
  
  p.Affiche()
  
  print("Volume du parallepipede: "+ str(p.Volume()))