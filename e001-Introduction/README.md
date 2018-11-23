## Identifiers. 

- An identifier is a word that represents elements of a programming language (variables, constants, names of methods, reserved words, ect).
- In python an identifier is defined as follows:
    - Start with a letter or an underscore (_). The following characters can be letters, digits and underscore.
    - Uppercase letters are distinguished from lowercase letters.
    - There is no maximum length established for the identifier.
    - Python doesn't allow punctuation such as @, $ and%, except the underscore (_).
    - By convention, we will not use identifiers that start with a capital letter.


## Reserved words.

- The reserved words are predefined identifiers to describe the structure of the program and, therefore, can not be used as identifiers created by the user in the programs.
- Python reserved words:

    |          |         |        |        |       |
    |----------|---------|--------|--------|-------|
    | and      | del     | from   | not    | while |
    | as       | elif    | global | or     | with  |
    | assert   | else    | if     | pass   | yield |
    | break    | except  | import | print  |
    | class    | exec    | in     | raise  |
    | continue | finally | is     | return | 
    | def      | for     | lambda | try    |
    
    
## Variables

- A variable is a space to store modifiable data, in the memory of a computer.
- In Python, a variable is defined with the syntax:
    
    > name = value
    
- By convention the snake_case nomenclature is used, the names are written in lowercase letters and for compound names (_) is used.
    
    ``` 
    my_first_variable = 32
    ```
    
    
## Constants

- Type of "variable" used to define values that will not be modified.
- The names are written in uppercase letters.

    ``` 
    MY_FIRST_CONSTANT = 3.1416
    ```
    
- Actually, in Python there are no constants, if we declare a "constant" and later modify it supposedly this change should not have an effect, but if we print the values before and after the modification we will see that it is modified.
- This occurs due to the dynamic python typing. The reality is that in python all are objects, this concept we will see later.
    
    
## Type of data

- Text (string):

    ``` 
    my_string = "Hello World!"
    ```
     
    ``` 
    my_string_multiline = """
    This is a chain
    of several lines
    """
    ```
    
- Integer number:

    ``` 
    age = 21
    ```

- Octal integer:

    ``` 
    age = 021
    ```

- Hexadecimal integer number:

    ``` 
    age = 0x21
    ```

- Real number:

    ``` 
    price = 52.99
    ```

- Boolean (true / False):

    ``` 
    true = True
    false = False
    ```
    
- Later we will see more


## Arithmetic Operators

    | Symbol | Meaning        | Example    | Result |
    |--------|----------------|------------|--------|
    | +      | sum            | a = 6 + 5  | 11     |
    | -      | subtraction    | a = 6 - 5  | 1      |
    | -      | negation       | a = - 5    | -5     |
    | *      | Multiplication | a = 6 * 5  | 30     |
    | **     | Exponent       | a = 2 ** 3 | 8      |
    | /      | Division       | a = 6 / 5  | 1.2    |  
    | //     | Whole division | a = 6 // 5 | 1.0    |  
    | %      | Module         | a = 6 % 5  | 1      |
    
    
## Comments.

- The comments help to understand the program code.

    ```
    # comment in one line
    age = 21
    
    """
    comments in
    more than
    one line
    """
    age = 21
    
    age = 21    # comment in one line
    ```
    

## Data entry by console.

- To capture data entered by console it is important to take into account the version of Python that we are using.
- In Python 3 only the function input() is used, in this way we will read any data as a text string, that is to read numbers we must convert the string to type number.
- In Python 2, input() is used for reading numbers and raw_input() for text strings.

    ```
    # Data entry by console
    # Python 3
    print("Write your name: ")
    name = input()
    print(f"Your name is: {name}")
    print(type(name))       # type() returns the data type of the variable
    
    print("-----------------------")
    print("Write your age: ")
    age = input()
    print(f"Your age is: {age}")
    print(type(age))
    age = int(age)      # With int() we casted the data to numeric type
    print(type(age))
    ```    
























