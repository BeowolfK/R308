def dire_bonjour_a(nom):
    if nom == "" or not isinstance(nom, str):
        raise NameError(f"nom \"{nom}\" n'est pas une chaine de caractère")
    print("Bonjour", nom)

try:
    dire_bonjour_a("Kénan")
except NameError as err:
    print(err)

try:
    dire_bonjour_a("")
except NameError as err:
    print(err)

try:
    dire_bonjour_a(5)
except NameError as err:
    print(err)
