print("##################### 1 #####################")
from io import open

file = open("file.txt", "w")
file.write("Hello world!!!")
file.close()

file = open("file.txt", "r")
print(file.read())
file.close()

"""
output:
    Hello world!!!
"""


print("##################### 2 #####################")
file = open("file.txt", "a")
file.write("""
more lines
more lines
more lines""")
file.close()

file = open("file.txt", "r")
print(file.read())
file.close()

"""
output:
    Hello world!!!
    more lines
    more lines
    more lines
"""
