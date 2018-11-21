# Control Flow Statements

## Iterative Statements

- Unlike conditional control structures, iterative ones (loops), allow us to execute the same code, repeatedly, while one condition is met.
- In Python there are two cyclic structures available:
    - The while loop
    - The for loop

### While loop   

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

##### break

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

### For loop 

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
    
- Another way to iterate with the for loop that can emulate the while loop:

    ```
    for num in range(0, 5):
        print(num)
    
    """
    Output:
        0
        1
        2
        3
        4
    """
    ```    
    
    
### Complementary instructions to the loops

##### continue

- This instruction causes you to return to the beginning of the loop, ignoring the other instructions and moving on to the next iteration.

    ```
    sentence = "I just want you to count the letters"
    counter = 0
    print(len(sentence))
    
    for letter in sentence:
        if letter == ' ':
            continue
        counter+=1
    
    print(counter)
    
    """
    Output:
        36
        29
    """
    ```

##### pass

- It is a null operation, so nothing happens when it is executed.
- It is used when a declaration is required by syntax but you do not want to execute any code.
- It is also used in places where the code has not yet been written (using it as a temporary filling, until the final code is written).

    ```
    sentence = "I just want you to count the letters"
    counter = 0
    print(len(sentence))
    
    for letter in sentence:
        pass    # Incomplete code
    
    print(counter)
    
    """
    Output:
        36
        0
    """
    ``` 
       

##### else

- You can use the 'else' instruction in a loop, you have to be careful as it can confuse us.
- The code of this instruction is executed when all the iterations of a loop are completed.       

    ```
    sentence = "Count only the length of the first word"
    counter = 0
    
    for letter in sentence:
        counter += 1
        if letter == ' ':
            break
    else:
        counter = 0
        print("It was not a sentence, it was a word")
    
    print(counter)
    
    
    sentence = "Test"
    counter = 0
    
    for letter in sentence:
        counter += 1
        if letter == ' ':
            break
    else:
        counter = 0
        print("It was not a sentence, it was a word")
    
    print(counter)
    
    """
    Output:
        6
        It was not a sentence, it was a word
        0
    """
    ```