import sys

print()

arg_start = sys.argv[1]

for letter in range(ord(arg_start) , ord("z") + 1):
    print(chr(letter), end="")
    
print()