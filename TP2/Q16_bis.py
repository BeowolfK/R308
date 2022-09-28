from Q16 import Etudiant

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
print(e.Affiche())

print("Modification de la moyenne")
while True:
    try:
        e.set_Moyenne(float(input("moyenne : ")))
        break   
    except:
        print("erreur dans les données")
        print("reprendre")
        print("fermeture de l'application")
print(e.Affiche())