import sys
import re

arg_count = 0
for arg in sys.argv:
    arg_count += 1

if arg_count != 2:
    print("erreur: il faut un argument")
    sys.exit()

time_24 = sys.argv[1]
pattern = r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$" # regEx pour HH:MM

if not re.match(pattern, time_24):
    print("erreur: Respectez le format HH:MM et les plages horaires, 24h.")
    sys.exit()

hour_24, minutes = time_24.split(":")
hour_24 = int(hour_24)
minutes = int(minutes)

if hour_24 == 0:
    meridiem = "AM"
    hour_12 = 12
elif (1 <= hour_24 <= 11):
    meridiem = "AM"
    hour_12 = hour_24
elif hour_24 == 12:
    meridiem = "PM"
    hour_12 = 12
else:
    meridiem = "PM"
    hour_12 = hour_24 - 12

print(f"{hour_12}:{minutes:02}{meridiem}")

# 11:35
# 23:47
# 24:44
# 01:01
# 75:45
# 31:19
# 26:45
# 11:60
# 1:33