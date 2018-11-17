## Control Flow Statements

### Iterative Statements

- Unlike conditional control structures, iterative ones (loops), allow us to execute the same code, repeatedly, while one condition is met.
- In Python there are two cyclic structures available:
    - The while loop
    - The for loop

#### While loop   

- This loop is responsible for executing the same action "while" a certain condition is fulfilled.

    ```
    a = 0
    while a<5:
        print(a)
        a+=1
    
    """
    Output:
        0
        1
        2
        3
        4
    """
    ```

- If you look at the last line:

    ```
    a += 1
    ```

- You will notice that in each iteration, we increase the value of the variable that conditions the loop (a). If we did not, this variable would always be the same and the loop would run infinitely.
- But, what happens if the value that conditions the iteration is not numeric and can not increase? In that case, we can use a conditional control structure, nested inside the loop, and stop the execution when the conditional stops fulfilling the reserved keyword "break".
    
    ```
    a = 0
    while True:
        a += 1
        print(a)
        if a == 3:
            break
            
    """
    Output:
        1
        2
        3
    """
    ```

#### For loop 

- The for loop, in Python, is the one that will allow us to iterate over a complex variable of the list or tuple type.

    ```
    color_list = ['red', 'blue', 'green']
    
    for color in color_list:
        print(color)
    
    """
    Output:
        red
        blue
        green
    """
    ```
    
- Later we will see more uses.