# Files

- The objective of the use of external files is the persistence of data, another more advanced alternative would be the use of databases that we will see later.
- There are two ways to work with external files, through the module "os", this module facilitates the work with the whole system of files and directories at the level of the operating system, the second option is simpler and we will work at the level of the application treating files as objects.
- We can distinguish four basic phases in the management of files, the first would be the creation, the second the opening of the created file, the third the manipulation of this, and finally the closing of the file.


### Open files

- The first thing we need to work with a file is to create a File object and assign it a value.
- To assign a variable with a file type value, it is only necessary to use the integrated function open(), which is intended for the opening of a file.
- This function receives two parameters, the route, and the opening mode.


### Opening Modes
 
- With the opening mode we refer to what we are going to do with the file, that is, if we are going to read the file, write it, read and write, etc.
- It is necessary to know that every time we open a file we are creating a pointer, which will be positioned within the file in a specific place (at start or end) and this pointer will be able to move inside that file, choosing its new position, by means of the corresponding byte number.


| Instruction | Opening mode                                                           |
|-------------|------------------------------------------------------------------------|
| r           | Read only.                                                             | 
| rb          | Same as "r" but in binary mode.                                        | 
| r+          | Reading and writing.                                                   |   
| rb+         | Same as "r+" but in binary mode.                                       | 
| w           | Only writing. Create the file, and if it exists, overwrite it.         |  
| wb          | Same as "w" but in binary mode.                                        |
| w+          | Reading and writing. Create the file, and if it exists, overwrite it.  | 
| wb+         | Same as "w+" but in binary mode.                                       | 
| a           | Added (add content). Create the file if it does not exist.             |   
| ab          | Same as "a" but in binary mode.                                        | 
| a+          | Added (add content) and writing. Create the file if it does not exist. | 
| ab+         | Same as "a+" but in binary mode.                                       |


- In all the pointer is located at the beginning of the file less in the indicators that contain an "a", that in the case that the file exists, the pointer will be located at the end of the file.
- Basic examples: 

    ```
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
    ```
    
    ```
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
    ```
    
### Methods of file    
    
##### read()

- Read all the contents of a file.
- If the length of bytes is passed, it will read only the content up to the indicated length.

    ```
    file = open("file.txt", "r")
    print(file.read(5))
    file.close()
    
    """
    output:
        Hello
    """
    ``` 
    
##### readline()

- Read a line from the file.
- If the length of bytes is passed, it will read only the content up to the indicated length.

    ```
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
    ``` 
    
##### readlines()

- Read all the lines of a file and return them as a list.
- If the length of bytes is passed, it will read only the content up to the indicated length.

    ```
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
    ```      
    
##### write()

- Write in the file.

    ```
    file = open("file.txt", "a")
    file.write("\nwriting...")
    file.close()
    ``` 
    
##### writelines()

- An iterable object (as a list) is passed to it by parameter and it writes each value from line to line in the file.

    ```
    file = open("file.txt", "a")
    file.writelines(["\nwrite", " lines"])
    file.close()
    ``` 
        
##### seek()

- Move the pointer to the indicated byte.

    ```
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
    ```    
               
##### tell()

- Returns the current position of the pointer.

    ```
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
    ```        
    

### File properties

##### closed

- Returns true or false depending on whether the file has been closed or not.

##### mode

- Returns the opening mode.

##### name

- Returns the name of the file.

##### encoding

- Returns the character encoding of a text file.


```
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
```


### Automatic closing

##### Use of "with"

```
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
```

- In this way we can work with a file without having to close it since at the end of the "with" block the method "close()" is invoked automatically