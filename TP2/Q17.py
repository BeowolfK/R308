from Q16 import Etudiant

class groupeEtudiant:
  def __init__(self, taille):
    if taille <5:
      raise ValueError("Taille trop petite")
    self.__taille = taille
    self.__etudiants = [None] * taille

  def ajouter(self, Etudiant, position):
    self.__etudiants[position] = Etudiant.Affiche()

  def etudiantNo(self, position):
    return self.__etudiants[position]

  def affiche(self):
    print("Taille: "+ str(self.__taille)+", etudiants:"+ str(self.__etudiants))

  def effacer(self, position):
    self.__etudiants[position] = None
    
