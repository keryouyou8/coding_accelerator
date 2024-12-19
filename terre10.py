import sys

print()

arg_count = 0
for arg in sys.argv:
    arg_count += 1

if arg_count != 2:
    print("erreur : Seul un argument est requis.")
    sys.exit()

input_number = sys.argv[1]

if not input_number.lstrip("-").isdigit() or int(input_number) <= 1:
    print("erreur : Entrez un entier positif supérieur à 1.")
    sys.exit()

input_number = int(input_number)

is_prime = True
# print("racine carré: " , int(number ** 0.5))
# print()

for i in range(2, int(input_number ** 0.5) + 1):
    # print("i : " , i)
    if input_number % i == 0:
        # print("le reste de number % i == 0 : ", number % i == 0)
        # print()
        
        is_prime = False
        break
    # else: 
    #     print("le reste de number % i == 0 : ", number % i == 0)
    #     print()

# print("is_prime : " , is_prime)
# print()

if is_prime:
    print(f"Oui, {input_number} est un nombre premier.")
else:
    print(f"Non, {input_number} n’est pas un nombre premier.")