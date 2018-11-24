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


print("##################### 3 #####################")
file = open("file.txt", "r")
print(file.read(5))
file.close()

"""
output:
    Hello
"""


print("##################### 4 #####################")
file = open("file.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline(5))
file.close()

"""
output:
    Hello world!!!
    
    more lines
    
    more 
"""


print("##################### 5 #####################")
file = open("file.txt", "r")
print(file.readlines(5))
print(file.readlines())
print(file.readlines())
file.close()

"""
output:
    ['Hello world!!!\n']
    ['more lines\n', 'more lines\n', 'more lines']
    []
"""


print("##################### 6 #####################")
file = open("file.txt", "a")
file.write("\nwriting...")
file.close()


print("##################### 7 #####################")
file = open("file.txt", "a")
file.writelines(["\nwrite", " lines"])
file.close()


print("##################### 8 #####################")
file = open("file.txt", "r")
print("### read 1 ###\n" + file.read())
print("### read 2 ###\n" + file.read())
file.seek(0)
print("### read 3 ###\n" + file.read())
file.close()

"""
output:
    ### read 1 ###
    Hello world!!!
    more lines
    more lines
    more lines
    ### read 2 ###

    ### read 3 ###
    Hello world!!!
    more lines
    more lines
    more lines
"""


print("##################### 9 #####################")
file = open("file.txt", "r")
print(file.tell())
print(file.read(5))
print(file.tell())
print(file.readlines())
print(file.tell())
file.close()

"""
output:
    0
    Hello
    5
    [' world!!!\n', 'more lines\n', 'more lines\n', 'more lines']
    47
"""


print("##################### 10 #####################")
file = open("file.txt", "r")
print(file.closed)
print(file.mode)
print(file.name)
print(file.encoding)
file.close()
print(file.closed)

"""
output:
    False
    r
    file.txt
    UTF-8
    True
"""


print("##################### 11 #####################")
with open("file.txt", "r") as file:
    print(file.read())

print("\n### is closed? ###\n" + str(file.closed))

"""
output:
    Hello world!!!
    more lines
    more lines
    more lines
    writing...
    write lines
    
    ### is closed? ###
    True
"""