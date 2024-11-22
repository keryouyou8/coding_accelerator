# Version 2 en utilisant le ASCII
first_letter = "a"
last_letter = "z"

for letter in range(ord(first_letter), ord(last_letter) + 1):  # 97 = 'a', 123 = 'z' + 1
    print(chr(letter), end="")