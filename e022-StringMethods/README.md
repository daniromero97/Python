# String methods

- We are going to see some of the methods of the String class in a generic way.


### Formatting methods

##### capitalize()
 
- Convert the first letter to capitals.
    
    ```
    sentence = "this IS a TEST sentence."
    print(sentence)
    print(sentence.capitalize())
    
    """
    output:
        this IS a TEST sentence.
        This is a test sentence.
    """
    ```

##### upper()

- Convert a string to uppercase.

    ```
    print("##################### 1 #####################")
    print(sentence)
    print(sentence.upper())
    
    """
    output:
        this IS a TEST sentence.
        THIS IS A TEST SENTENCE.
    """
    ```

##### lower()
 
- Convert a string to lowercase.

```

```

##### swapcase()
 
- Convert uppercase to lowercase and vice versa.

    ```
    print(sentence)
    print(sentence.swapcase())
    
    """
    output:
        this IS a TEST sentence.
        THIS is A test SENTENCE.
    """
    ```

##### title()
 
- Convert a string to title format, that is, the first letter of each word in capital letters.

    ```
    print(sentence)
    print(sentence.title())
    
    """
    output:
        this IS a TEST sentence.
        This Is A Test Sentence.
    """
    ```

##### center(lenght, "caracter")
 
- Center a text

    ```
    print(sentence)
    print(sentence.center(40, "-"))
    
    """
    output:
        this IS a TEST sentence.
        --------this IS a TEST sentence.--------
    """
    ```

##### ljust(lenght, "caracter")
 
- Align a text to the left

    ```
    print(sentence)
    print(sentence.ljust(40, "-"))
    
    """
    output:
        this IS a TEST sentence.
        this IS a TEST sentence.----------------
    """
    ```

##### rjust(lenght, "caracter")
 
- Align a text to the right

    ```
    print(sentence)
    print(sentence.rjust(40, "-"))
    
    """
    output:
        this IS a TEST sentence.
        ----------------this IS a TEST sentence.
    """
    ```

##### zfill(lenght)
 
- Fill a text by prepending zeros

    ```
    print(sentence)
    print(sentence.zfill(40))
    
    """
    output:
        this IS a TEST sentence.
        0000000000000000this IS a TEST sentence.
    """
    ```