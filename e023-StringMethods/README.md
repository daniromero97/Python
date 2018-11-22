# String methods

### Substitution methods

##### format()
 
- Format a string, replacing text dynamically
    
    ```
    sentence = "My name is {0}"
    print(sentence)
    print(sentence.format("Dani"))
    
    """
    output:
        My name is {0}
        My name is Dani
    """
    ```
    
    ```
    sentence = "My name is {0} and I am {1} years old"
    print(sentence)
    print(sentence.format("Dani", 21))
    
    """
    output:
        My name is {0} and I am {1} years old
        My name is Dani and I am 21 years old
    """
    ```
    
    ```
    sentence = "My name is {name} and I am {age} years old"
    print(sentence)
    print(sentence.format(name="Dani", age=21))
    
    """
    output:
        My name is {name} and I am {age} years old
        My name is Dani and I am 21 years old
    """
    ```
    
    ```
    sentence = "{years} years are {days} days"
    print(sentence)
    print(sentence.format(years=21, days=21*365))
    
    """
    output:
        {years} years are {days} days
        21 years are 7665 days
    """    
    ```

##### replace()

- Replace text in a string.

    ```
    search = "the_name"
    replace = "Dani"
    print("My name is the_name".replace(search, replace))
    
    """
    output:
        My name is Dani
    """
    ```
    
##### strip()

- Remove characters to the left and right of a string.

    ```
    sentence = "      This is a test sentence     "
    print(sentence)
    print(sentence.strip())
    
    sentence = "----------This is a test sentence**********"
    print(sentence)
    print(sentence.strip('*'))
    print(sentence.strip('-').strip('*'))
    
    """
    output:
              This is a test sentence     
        This is a test sentence
        ----------This is a test sentence**********
        ----------This is a test sentence
        This is a test sentence
    """
    ```   
    
##### lstrip()

- Remove characters to the left of a string.

    ```
    sentence = "*********This is a test sentence**********"
    print(sentence)
    print(sentence.lstrip('*'))
    
    """
    output:
        *********This is a test sentence**********
        This is a test sentence**********
    """
    ```
    
##### rstrip()

- Remove characters to the right of a string.

    ```
    sentence = "*********This is a test sentence**********"
    print(sentence)
    print(sentence.rstrip('*'))
    
    """
    output:
        *********This is a test sentence**********
        *********This is a test sentence
    """
    ```