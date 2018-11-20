# OOP Functions

#### issubclass

- Returns true or false depending on whether one class is a subclass of another.

    ```
    print(issubclass(Car, Vehicle))
    
    """
    output:
        True
    """
    ```


#### isinstance

- Returns true or false depending on whether one object is a instance of a class.

    ```
    print(isinstance(c, Vehicle))
    print(isinstance(m, Vehicle))
    print(isinstance(c, Motorcycle))
    
    """
    output:
        True
        True
        False
    """
    ```


#### dir

- Returns an alphabetically sorted list of methods and properties of some object.

    ```
    print(dir(c))
    
    """
    output:
        ['_Car__trailer', '_Vehicle__brand', '_Vehicle__weight', '_Vehicle__wheels', '__class__', '__delattr__', 
        '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
        '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
        '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'properties']
    """
    ```


#### vars

- Returns a dictionary of attributes and values of the obj object.

    ```
    print(vars(c))
    
    """
    output:
        {'_Vehicle__wheels': 4, '_Vehicle__weight': 1200, '_Vehicle__brand': 'Audi', '_Car__trailer': True}
    """
    ```


#### getattr

- Returns the value of the indicated attribute.

    ```
    print(getattr(c, '_Vehicle__brand', 'None'))
    
    """
    output:
        Audi
    """
    ```
    
    
#### setattr

- Overwrite an attribute of an object with the indicated value.
- If it does not exist, create it and assign the value.

    ```
    print(setattr(c, '_Vehicle__brand', 'BMW'))
    print(getattr(c, '_Vehicle__brand', 'None'))
    print(setattr(c, 'name', 'my car'))
    print(getattr(c, 'name', 'None'))
    
    """
    output:
        None
        BMW
        None
        my car
    """
    ```


#### delattr

- Remove the indicated attribute from the object.
    
    ```
    print(delattr(c, 'name'))
    print(getattr(c, 'name', 'None'))
    
    """
    output:
        None
        None
    """
    ```