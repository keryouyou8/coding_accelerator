import sys

print()

arg_count = 0
for arg in sys.argv:
    arg_count += 1

if arg_count != 2:
    print("erreur: Problème d'argument.")
    sys.exit()

string_to_count = sys.argv[1]

if string_to_count.strip() == "" or string_to_count.isdigit():
    print("erreur : Il faut une chaîne de caractère.")
    sys.exit()
    
char_count = 0
for char in string_to_count:
    char_count += 1

print(char_count)