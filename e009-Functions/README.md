# Functions

- A function is defined with the instruction def followed by the name of the function and opening and closing parentheses.
- The definition ends with two points (:) and the code that composes it will be indented with 4 spaces.
- To execute a function it is called by its name.
    
    ```
    def function_name():
        print("Hello world!!!")

    function_name()
    
    """"
    output:
        Hello world!!!
    """ 
    ```

- The functions can return data and these be assigned to variables.

    ```
    def function_name():
        return "Hello world!!!"

    function_return = function_name()
    print(function_return)
    print(function_name())
    
    """"
    output:
        Hello world!!!
        Hello world!!!
    """
    ```    

    
### Parameters  

- The parameters are values that the function receives when called to be used in it.
- A function may not have parameters, have one, or several.
- Parameters are indicated in parentheses and separated by commas.
- The parameters used by the function are categorized as local variables, so they can only be used within it.  

    ```
    def sum(n, n2, n3):
        return n + n2 + n3
    
    function_return = sum(5, 7, 9)
    print(function_return)
    
    """"
    output:
        21
    """
    ```

    
### Default parameters

- Default values can be assigned to the parameters of the functions.
    
    ```
    def sum10(num, n=10):
        return num + n
    
    function_return = sum10(5)
    print(function_return)
    
    """"
    output:
        15
    """
    ```
    


### Keywords as parameters

- The arguments can be passed as key=value.    
    
    ```
    def sum10(num, n=10):
        return num + n
    
    function_return = sum10(num=15, n=20)
    print(function_return)
    
    """"
    output:
        35
    """
    ```
    

### Arbitrary parameters

- A function can receive an unknown number of parameters in the form of a tuple.
- A `*` must be prefixed to the tuple.  
- If the function receives fixed and arbitrary parameters, the arbitrary ones will always go after the fixed ones.  

    ```
    def greet(message, *names):
        all_names = ""
        for name in names:
            all_names += " >> %s << " % (name)
    
        return "%s %s" % (message, all_names)
    
    
    function_return = greet("Hi", "Dani", "Bea")
    print(function_return)
    
    """"
    output:
        Hi  >> Dani <<  >> Bea << 
    """
    ```
    
- You can also receive keywords as arbitrary parameters.
- They must go to the end and be preceded by `**`.    
    
    ```
    def greet(message, *names, **kwords):
        all_names = ""
        for name in names:
            all_names += " >> %s << " % (name)
    
        all_kwords = ""
        for kword in kwords:
            all_kwords += " >> key: %s << " % kwords[kword]
    
        return "%s %s and keys %s" % (message, all_names, all_kwords)
    
    
    function_return = greet("Hi", "Dani", "Bea", key1 = "k1", key2 = "k2")
    print(function_return)
    
    """"
    output:
        Hi  >> Dani <<  >> Bea <<  and keys  >> key: k1 <<  >> key: k2 << 
    """
    ```
    

### Unpacking of parameters

- We can also pass to a function a tuple or a dictionary.
- In the same way we will indicate that it is a tuple preceding it with `*` and a dictionary with `**`.

    ```
    def my_function(parameter1, parameter2):
        return "%s --- %s" % (parameter1, parameter2)
    
    function_return = my_function(*["p1", "p2"])
    print(function_return)
    
    function_return2 = my_function(**{"parameter1": "p1", "parameter2": "p2"})
    print(function_return2)
    
    """"
    output:
        p1 --- p2
        p1 --- p2
    """
    ```  