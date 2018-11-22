# Exceptions

- The exceptions are errors that occur during the execution of the program.
- The syntax is correct but something unexpected happens.
- At the moment when an exception appears, the program stops and the code stops executing.

    ```
    print("Division")
    print(5/0)
    print("End")
    
    """
    output:
        Division
        Traceback (most recent call last):
          File ".../Python/e020-Exceptions/Exceptions.py", line 1, in <module>
            print(5/0)
        ZeroDivisionError: division by zero
    """
    ```

### Exception control

- This type of exceptions can be controlled so that the execution of the program continues.

    ```
    print("Division")

    try:
        print(5/0)
    except ZeroDivisionError:
        print("It can not divide between zero.")
    
    print("End")
    
    """
    output:
        Division
        It can not divide between zero.
        End
    """
    ```    
    
- Use of the "try" and "except" instructions to control the error.
- In the block "try" go the instructions of the program to execute, and in the "except" the possible error will be captured.


### Control of more than one exception

- You can control more than one exception.

    ```
    print("Division")

    try:
        print((5/"test"))
        print(5/0)
    except ZeroDivisionError:
        print("It can not divide between zero.")
    except TypeError:
        print("The division has to be just numbers.")
    
    print("End")
    
    """
    output:
        Division
        The division has to be just numbers.
        End
    """    
    ```
    
- Simply add another "except" block with the possible exception.


### Finally

- If we want some part of our code to be executed, we can always use the "finally" instruction.

    ```
    print("Division")

    try:
        print((5/"test"))
        print(5/0)
    finally:
        print("End")
    
    """
    output:
        Division
        End
        Traceback (most recent call last):
            File ".../Python/e020-Exceptions/Exceptions.py", line 5, in <module>
            print((5/"test"))
        TypeError: unsupported operand type(s) for /: 'int' and 'str'
    """
    ```

- Imagining that we have forgotten to control some exception, we can make sure that there is some part of the code that always runs in spite of this.


        