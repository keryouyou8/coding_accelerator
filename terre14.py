import sys

arguments = sys.argv[1:]
arg_count = 0

for arg in arguments:
      arg_count += 1

if arg_count < 2:
      print("erreur : Il faut au moins 2 arguments")
      sys.exit()

for i in arguments:
        if not i.isdigit():
            print("erreur : Il faut que des chiffres comme argument.")
            sys.exit()

for i in range(arg_count - 1):
    if int(arguments[i]) > int(arguments[i+1]):
        print("Liste pas triée !")
        sys.exit()

print("Liste triée !")