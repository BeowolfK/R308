from Q15 import Personne

class Etudiant(Personne):
  def __init__(self):
    self.__Matiere = ""
    self.__Annee = 0
    self.__Moyenne = 0

  def set_Annee(self, annee):
    assert isinstance(annee, int)
    self.__Annee = annee

  def get_Annee(self):
    return self.__Annee

  def set_Matiere(self, matiere):
    assert isinstance(matiere, str)
    self.__Matiere = matiere

  def get_Matiere(self):
    return self.__nom

  def set_Moyenne(self, moyenne):
    assert isinstance(moyenne, float)
    self.__Moyenne = moyenne

  def get_Moyenne(self):
    return self.__Moyenne

  def Affiche(self):
    return [*super().Affiche(), self.__Annee, self.__Matiere, self.__Moyenne]
