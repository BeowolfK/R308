from Q17 import groupeEtudiant
from Q16 import Etudiant

def new_student():
    e = Etudiant()
    while True:
        try:
            e.set_Nom(input("nom : "))
            e.set_Prenom(input("prenom : "))
            e.set_Age(int(input("age : ")))
            e.set_Matiere(input("matiere : "))
            e.set_Annee(int(input("annee : ")))
            e.set_Moyenne(float(input("moyenne : ")))
            break   
        except Exception as err:
            print("erreur dans les données")
            print("reprendre")
            print("fermeture de l'application")
    return e


getud = groupeEtudiant(int(input("taille : ")))
while True:
    cmd = input("Add (a) Remove (r)  Display List (l) Display Student (s) Exit (e) : ").upper()
    if cmd == "A":
        st = new_student()
        pos = int(input("position : "))
        getud.ajouter(st, pos)
    elif cmd == "R":
        getud.effacer(int(input("position : ")))
    elif cmd == "L":
        getud.affiche()
    elif cmd == "S":
        print(getud.etudiantNo(int(input("position : "))))
    elif cmd == "E":
        exit(0)