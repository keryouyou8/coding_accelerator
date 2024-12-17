import sys

print()

arg_count = 0
for arg in sys.argv:
    arg_count += 1

if arg_count != 2:
    print("erreur: Problème d'argument.")
    sys.exit()

string_to_reverse = sys.argv[1]

if string_to_reverse.strip() == "":
    print("erreur: Le string est vide.")
    sys.exit()

reversed_string = ""
for i in range(len(string_to_reverse) - 1, -1, -1):
    reversed_string += string_to_reverse[i]

print(reversed_string)