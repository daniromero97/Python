# Encapsulation

- It is about hiding the properties of an object so that they are not accessible from outside that object.
- To hide an attribute in python, two underscore are prefixed to the name of the attribute.

    ```
    def __init__(self, name, height, weight, age):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
    ```
    
- And to access these attributes, we have to do it in the same way, putting two underscore first.

    ```
    def properties(self):
        print("Name: %s, height: %.2f m, weight: %.1f kg, age: %d years old" % (self.__name, self.__height, self.__weight, self.__age))    
    ```    

- In this way we can no longer access the attributes from outside the class.

    ```
    p1 = Person("Gonzalo", 1.78, 74, 25)
    p1.properties()
    
    p1.__name = "Luis"
    p1.properties()
    print(p1.__name)    # Unresolved attribute reference '__name' for class 'Person'
    
    """
    output:
        Name: Gonzalo, height: 1.78 m, weight: 74.0 kg, age: 25 years old
        Name: Gonzalo, height: 1.78 m, weight: 74.0 kg, age: 25 years old
        Luis
    """    
    ```

- In python it is not totally effective, because if we know the name of the attribute if we can "modify" it.
- In python all methods and attributes are public. By convention, they are said to be private when they start with double underscore.   
    

    

    