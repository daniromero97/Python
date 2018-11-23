# String methods

### Validation Methods

##### startswith()
 
- Know if a string starts with a given substring.
    
    ```
    sentence = "This is a test sentence."
    print(sentence)
    print(sentence.startswith("This"))
    print(sentence.startswith("this"))
    print(sentence.startswith("this", 5))
    
    """
    output:
        This is a test sentence.
        True
        False
        False
    """
    ```
    
##### endswith()
 
- Know if a string ends with a given substring.
    
    ```
    sentence = "This is a test sentence."
    print(sentence)
    print(sentence.endswith("sentence."))
    print(sentence.endswith("ence."))
    print(sentence.endswith("a", 5, 10))
    
    """
    output:
        This is a test sentence.
        True
        True
        False
    """
    ```   
    
##### isalnum()
 
- Know if a string is alphanumeric.
    
    ```
    sentence = "This is a test sentence."
    print(sentence)
    print(sentence.isalnum())
    
    sentence = sentence.replace(" ", "")
    print(sentence)
    print(sentence.isalnum())
    
    sentence = sentence.replace(".", "")
    print(sentence)
    print(sentence.isalnum())
    
    """
    output:
        This is a test sentence.
        False
        Thisisatestsentence.
        False
        Thisisatestsentence
        True
    """
    ``` 
    
##### isalpha()
 
- Know if a string is alphabetic.
    
    ```
    sentence = "This is a test sentence."
    print(sentence)
    print(sentence.isalpha())
    
    sentence = sentence.replace(" ", "").replace(".", "")
    print(sentence)
    print(sentence.isalpha())
    
    """
    output:
        This is a test sentence.
        False
        Thisisatestsentence
        True
    """
    ```        
    
##### isdigit()
 
- Know if a string is numeric.
    
    ```
    sentence = "12345"
    print(sentence)
    print(sentence.isdigit())
    
    sentence = "123 45"
    print(sentence)
    print(sentence.isdigit())
    
    """
    output:
        12345
        True
        123 45
        False
    """
    ```
    
##### islower()
 
- Know if a string contains only lowercase.
    
    ```
    sentence = "the test"
    print(sentence)
    print(sentence.islower())
    
    sentence = "the test 100"
    print(sentence)
    print(sentence.islower())
    
    sentence = "the test ..."
    print(sentence)
    print(sentence.islower())
    
    """
        output:
        the test
        True
        the test 100
        True
        the test ...
        True
    """
    ```   
    
##### isupper()
 
- Know if a string contains only uppercase.
    
    ```
    sentence = "the test"
    print(sentence)
    print(sentence.isupper())
    
    sentence = sentence.capitalize()
    print(sentence)
    print(sentence.isupper())
    
    sentence = sentence.upper()
    print(sentence)
    print(sentence.isupper())
    
    """
        the test
        False
        The test
        False
        THE TEST
        True
    """
    ```    
    
##### isspace()
 
- Know if a string contains only blank spaces.
    
    ```
    sentence = "the test"
    print(sentence.isspace())
    
    sentence = "      ."
    print(sentence.isspace())
    
    sentence = "      "
    print(sentence.isspace())
    
    """
        False
        False
        True
    """
    ```
    
##### istitle()
 
- Know if a string has a Title Format.
    
    ```
    sentence = "the test"
    print(sentence.istitle())
    
    sentence = sentence.capitalize()
    print(sentence.istitle())
    
    sentence = sentence.title()
    print(sentence.istitle())
    
    """
        False
        False
        True
    """
    ```                             