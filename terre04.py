import sys

print()

arg_count = 0
for arg in sys.argv:
    arg_count += 1

if arg_count != 2:
    print("Tu ne me la mettras pas à l’envers.")
    sys.exit()

# Récupérer l'argument et vérifier si c'est un entier (+ ou -)
argument = sys.argv[1]
if not argument.lstrip("-").isdigit():
    print("Tu ne me la mettras pas à l’envers.")
    sys.exit()

# Convertir en entier et vérifier si pair ou impair
number = int(argument)
if number % 2 == 0:
    print("pair")
else:
    print("impair")