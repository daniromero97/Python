# Polymorphism

- Polymorphism is understood as the fact that a method has different executions or forms depending on the object that invokes it.

- Example:
    
    ```
    class Car(Vehicle):

    def __init__(self, wheels, weight, brand, trailer):
        super().__init__(wheels, weight, brand)
        self.__trailer = trailer

    def properties(self):
        super().properties()
        print("Trailer: %s" % self.__trailer)


    class Motorcycle(Vehicle):
    
    def __init__(self, wheels, weight, brand, sidecar):
         super().__init__(wheels, weight, brand)
         self.__sidecar = sidecar
    
    def properties(self):
         super().properties()
         print("Sidecar: %s" % self.__sidecar)
    ```

- Two objects that inherit from the same class and whose properties method acts differently depending on the object that invokes it.

    ```
    c = Car(4, 1200, "Audi", True)
    c.properties()
    
    m = Motorcycle(2, 700, "Honda", False)
    m.properties()
    
    """
    output:
        Wheels: 4, weight: 1200 kg, brand: Audi
        Trailer: True
        Wheels: 2, weight: 700 kg, brand: Honda
        Sidecar: False
    """    
    ```


 