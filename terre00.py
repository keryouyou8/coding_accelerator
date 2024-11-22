#Version 1
first_letter = "a"
last_letter = "z"

for letter in range(ord(first_letter), ord(last_letter) + 1):  # 97 = 'a', 123 = 'z' + 1
    print(chr(letter), end="")
    
#Version 2    
#alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#for lettre in alphabet:
#    print(lettre, end="")