import sys

arguments = sys.argv[1:]
arg_count = 0

for arg in arguments:
    arg_count += 1

if arg_count != 3:
    print("erreur : il faut 3 arguments.")
    sys.exit()

for i in arguments:
        if not i.isdigit():
            print("erreur : Il faut que des chiffres comme argument.")
            sys.exit()

first_number = int(arguments[0])
second_number = int(arguments[1])
third_number = int(arguments[2])

if first_number == second_number or first_number == third_number or second_number == third_number:
    print("erreur : Il faut des chiffres différents.")

if second_number < first_number < third_number or third_number < first_number < second_number:
     print(first_number)
     sys.exit()
elif first_number < second_number < third_number or third_number < second_number < first_number:
     print(second_number)
     sys.exit()
else:
     print(third_number)