## Control Flow Statements

- Code statements grouped in a controlled manner.
- The control flow of a Python program is regulated by conditional statements, loops, and function calls.


### Basic things
##### Indentation
    
- They are blocks of code separated from the left margin by 4 spaces or a tab.
- There are languages where it is not necessary to use it but it is always recommended since it gives greater readability to the code.
- In python its use is 100% necessary.    
     
    ```
    """
    Flow declarations
        expressions
        ...
        ...
    """    
    ```
    
    
##### Encoding

- The encoding is not more than a directive that is placed at the beginning of a Python file, in order to indicate to the system, the codification of characters used in the file.
- "utf-8" is a type of character encoding.
- If a character encoding is not indicated, Python might fail to find characters it is not able to recognize.

    ```
    # -*- coding: utf-8 -*-
    ```
    
    
##### Multiple assignment

- Possibility of assigning multiple variables in a single instruction.
    
    ```
    a, b, c = 'value', 2, False
    print(a)
    print(b)
    print(c)
    
    """
    Output:
        value
        2
        False
    """  
    ```
   
    
### Conditional Statements

- Conditional statements allow us to evaluate variables of our code to make our program behave in one way or another.
- One or more conditions can be evaluated and this will only yield two results: true or false.
- For example: if I'm hungry, I eat.
- To evaluate these conditions we have relational and logical operators.

#### Relational operators

| Symbol | Meaning               | Example | Result |
|--------|-----------------------|---------|--------|
| ==     | equal than            | 2 == 3  | False  |
| !=     | Different than        | 2 != 3  | True   |
| >      | Greater than          | 2 > 3   | False  | 
| <      | Smaller than          | 2 < 3   | True   |
| >=     | Greater than or equal | 2 >= 3  | False  |
| <=     | Smaller than or equal | 2 <= 3  | True   |
    
    
#### Logical operators    
    
| Operator | Example          | Result |
|----------|------------------|--------|
| and      | 2 == 2 and 3 > 4 | False  | 
| or       | 2 == 2 or 3 > 4  | True   | 
|          |                  |        | 
| xor      | 2 == 2 xor 3 > 4 | True   |    
| xor      | 2 < 2 xor 3 < 4  | True   |
| xor      | 2 == 2 xor 3 < 4 | False  |
| xor      | 2 < 2 xor 3 > 4  | False  |    
    

#### if Statement    

```
a, b = 5, 10

if a>b:
    print("'a' greater than 'b'")

if a<b:
    print("'a' smaller than 'b'")

"""
Output:
    'a' smaller than 'b'
"""
```


#### else Statement    

```
if a>b:
    print("'a' greater than 'b'")
else:
    print("'a' smaller than 'b'")

"""
Output:
    'a' smaller than 'b'
"""
```


#### elif Statement    

```
a, b, c = 2, 3, 4

if a>b and a>c:
    print("'a' is the biggest")
elif b>a and b>c:
    print("'b' is the biggest")
else:
    print("'c' is the biggest")

"""
Output:
    'c' is the biggest
"""
```