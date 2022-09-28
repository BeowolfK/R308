value = ""
while True:
    try:
        value = int(input("Entrez un nombre: "))
        break
    except ValueError:
        print("La valeur entré n'est pas un nombre")
print("Valeur correcte: " + str(value))
