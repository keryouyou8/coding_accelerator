import sys
import re

print()

arg_count = 0
for arg in sys.argv:
    arg_count += 1

if arg_count != 2:
    print("erreur: il faut un argument")
    sys.exit()

time_12 = sys.argv[1]
pattern = r"^(1[0-2]|0?[1-9]):([0-5][0-9])(AM|PM)$" # regEx pour HH:MM AM/PM
match = re.match(pattern, time_12)
# meridiem = time_12[-2:]

if not match:
    print("erreur: Respectez le format HH:MM AM/PM et les plages horaires, 24h.")
    sys.exit()

hour_12 = int(match.group(1))
minutes = int(match.group(2))
meridiem = match.group(3)

if meridiem == "PM" and hour_12 != 12:
    hour_24 = hour_12 + 12
elif meridiem == "AM" and hour_12 == 12:
    hour_24 = 0
else:
    hour_24 = hour_12

print(f"{hour_24:02}:{minutes:02}")