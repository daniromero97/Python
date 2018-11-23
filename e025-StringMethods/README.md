# String methods

### Methods of union and division

##### join()
 
- The join() is a string method which returns a string concatenated with the elements of an iterable.
- The join() method provides a flexible way to concatenate string. It concatenates each element of an iterable (such as list, string and tuple) to the string and returns the concatenated string.
    
    ```
    sequence = ("This is a ", "")
    s = "test"
    sentence = s.join(sequence)
    print(sentence)
    
    sequence = ("This is a ", " (", ")")
    sentence = s.join(sequence)
    print(sentence)
    
    """
    output:
        This is a test
        This is a test (test)
    """
    ```
    
##### partition()
 
- Split a string into three parts using a separator and return it in a tuple.
  
    ```
    sentence = "this is a test"
    separator = "is a"
    tuple = sentence.partition(separator)
    print(tuple)
    
    """
    output:
        ('this ', 'is a', ' test')
    """
    ``` 
    
##### split()
 
- Split a string into parts using a separator and return it as a list.
  
    ```
    sentence = "this is a test, " * 4
    separator = ","
    list = sentence.split(separator)
    print(sentence)
    print(list)
    
    """
    output:
        this is a test, this is a test, this is a test, this is a test, 
        ['this is a test', ' this is a test', ' this is a test', ' this is a test', ' ']
    """
    ```
    
        
##### splitlines()
 
- Separate a string in as many parts as lines have and return it in the form of a list.
  
    ```
    sentence = """line 1
    line2 
    line3"""
    
    print(sentence)
    print(sentence.splitlines())
    
    """
    output:
        line 1
        line2 
        line3
        ['line 1', 'line2 ', 'line3']
    """
    ```                                   