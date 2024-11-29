# Version 1
import sys

path = sys.argv[0]
file_name = ""

for char in path:
    if char == '/' : 
        file_name = ""
    else:
        file_name += char 

print(file_name)



# Version 2
# file_name = ""

# for char in path[::-1]:  
#     if char == '/':  
#     file_name = char + file_name  

# print(file_name)



# Version 3
# import sys

# path = sys.argv[0]
# file_name = path.split("/")[-1]

# print(file_name)



# Version 4
# file_name = __file__.split("\\")[-1]

# print(file_name)