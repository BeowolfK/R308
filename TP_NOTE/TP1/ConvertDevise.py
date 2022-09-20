"""
@author: Kénan Meylan TP1
Application de changement de devise entre euro, dollar et yuan
"""

from Conversion import Devise

def main():
    input 
    devise = Devise()
    while True:
        symbole = input("Entrez une devise EU, US ou YA : ")
        if symbole not in ["EU", "US", "YA"]: 
            exit(0)
        value = eval(input("Entrez une somme a convertir dans cette devise : "))
        devise.deviseConvert(symbole, value)
        print(f"Valeur en euro : {devise.euro}")
        print(f"Valeur en dollar : {devise.dollar}")
        print(f"Valeur en yuan : {devise.yuan}")

if __name__ == '__main__':
    main()
   