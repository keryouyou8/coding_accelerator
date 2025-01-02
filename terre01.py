import sys

path = sys.argv[0]
file_name = ""

for char in path:
    if char == '/' : 
        file_name = ""
    else:
        file_name += char 
        
print(file_name)