## Tuples

- Very similar to the lists.
- A tuple is an immutable list. A tuple can not change in any way once created.
- They are defined the same as the list but the elements are enclosed in parentheses and not in brackets.
- Like the lists, they have an order and start at position 0.
- You can use negative indexes as in the lists.
- Slicing also works, with this we get a new tuple.
- <strong> They are faster than the lists. </strong>
    
    
    ```
    my_tuple = ("value 1", "value 2", "value 3", ["value 4.1", "value 4.2"], 5, ("value 6.1", "value 6.2"))
    
    print(my_tuple)
    print(my_tuple[0])
    print(my_tuple[-1])
    print(my_tuple[2:5])
    
    
    """
    Output:
        ('value 1', 'value 2', 'value 3', ['value 4.1', 'value 4.2'], 5, ('value 6.1', 'value 6.2'))
        value 1
        ('value 6.1', 'value 6.2')
        ('value 3', ['value 4.1', 'value 4.2'], 5)
    """
    ```


### Applications

##### index and in

- Tuples are immutable, so you can not add, delete or modify elements.
- You can <strong> search </strong> for items in a tuple.
    
    ```
    print(my_tuple.index("value 2"))
    print(5 in my_tuple)
    
    """
    Output:
        1
        True
    """
    ```  
    
    
##### len and count
    
 - You can see the <strong> length </strong> of a tuple and <strong> count </strong> how many times a value appears.
 
     ```
    print(len(my_tuple))
    print(my_tuple.count("value 3"))
    
    """
    Output:
        6
        1
    """
    ``` 
    

##### max and min
    
- You can obtain the <strong> maximum and minimum </strong> value (if it is a tuple of integers).

     ```
    my_tuple2 = (1, 4, 5, 21, 2)
    print(min(my_tuple2))
    print(max(my_tuple2))
    
    """
    Output:
        1
        21
    """
    ``` 
    

##### list and tuple
    
- A tuple can be converted to list and a list to tuple.

     ```
    print(my_tuple)
    l = list (my_tuple)
    print(l)
    t = tuple (l)
    print(t)
    
    """
    Output:
        ('value 1', 'value 2', 'value 3', ['value 4.1', 'value 4.2'], 5, ('value 6.1', 'value 6.2'))
        ['value 1', 'value 2', 'value 3', ['value 4.1', 'value 4.2'], 5, ('value 6.1', 'value 6.2')]
        ('value 1', 'value 2', 'value 3', ['value 4.1', 'value 4.2'], 5, ('value 6.1', 'value 6.2'))
    """
    ``` 