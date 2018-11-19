# Functions

### Return calls

- It is possible to call a function within another function.
    
    ```
    def greet():
        return "Hello world"
    
    def full_greeting(name):
        return "%s and hello %s" % (greet(), name)
    
    print(full_greeting("Dani"))
    
    """"
    output:
        Hello world and hello Dani
    """
    ```
    
- But, what happens if we do not know the name of the function to invoke?
- To call functions dynamically, Python has two native functions: locals() and globals().
- These functions return a dictionary.
- locals() is composed of all the elements of local scope and globals() of global scope elements.

    ```
    def greet():
        return "Hello world"
    
    def full_greeting(name, function=""):
        return "%s and hello %s" % (globals()[function](), name)
    
    print(full_greeting("Dani", "greet"))
    
    print(locals()["full_greeting"]("Dani", "greet"))
    
    """"
    output:
        Hello world and hello Dani
        Hello world and hello Dani
    """
    ```


### How to know if a function exists

- To check if it exists we will use "in".
- And to check if the function can be called we will use the callable() function. 

    ```
    def greet():
        return "Hello world"
    
    def full_greeting(name, function=""):
        r = "error"
        if function in globals():
            if callable(globals()[function]):
                r = "%s and hello %s" % (globals()[function](), name)
        return r
    
    print(full_greeting("Dani", "greet"))
    print(full_greeting("Dani", "greeeeet"))
    
    
    if "full_greeting" in locals():
        if callable(locals()["full_greeting"]):
            print(locals()["full_greeting"]("Dani", "greet"))
    
    
    """"
    output:
        Hello world and hello Dani
        error
        Hello world and hello Dani
    """
    ```


    