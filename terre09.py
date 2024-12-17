import sys

print()

arg_count = 0
for arg in sys.argv:
    arg_count += 1

if arg_count != 2:
    print("erreur : Un seul argument est requis.")
    sys.exit()

number = sys.argv[1]

if not number.lstrip("-").isdigit():
    print("erreur : L'argument doit être un nombre entier.")
    sys.exit()

number = int(number)

if number < 0:
    print("erreur : Le nombre doit être positif.")
    sys.exit()

square_root = 0
found = False

for i in range(number + 1):
    if i * i == number:
        square_root = i
        found = True
        break

if found:
    print(square_root)
else:
    print("erreur : Pas de racine carrée exacte pour ce nombre.")
