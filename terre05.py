import sys

arg_count = 0
for arg in sys.argv:
    arg_count += 1

if arg_count != 3:
    print("erreur : Deux arguments requis.")
    sys.exit()

numerator = sys.argv[1]
denominator = sys.argv[2]
if not numerator.isdigit() or not denominator.isdigit():
    print("erreur: Il faut des pas de lettre dans une division, chef.")
    sys.exit()

numerator = int(numerator)
denominator = int(denominator)

if denominator == 0 or denominator > numerator:
    print("erreur: Le denominateur à un problème là.")
    sys.exit()

result = numerator // denominator
remainder = numerator % denominator

print(f"resultat: {result}")
print(f"reste: {remainder}")