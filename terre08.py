import sys

arg_count = 0
for arg in sys.argv:
    arg_count += 1

if arg_count != 3:
    print("erreur : Deux arguments requis.")
    sys.exit()

base = sys.argv[1]
exponent = sys.argv[2]

if not base.lstrip("-").isdigit() or not exponent.lstrip("-").isdigit():
    print("erreur : Les arguments doivent être des nombres entiers.")
    sys.exit()

base = int(base)
exponent = int(exponent)

if exponent < 0:
    print("erreur : L'exposant ne peut pas être négatif.")
    sys.exit()

result = 1
for i in range(exponent):
    result *= base

print(result)