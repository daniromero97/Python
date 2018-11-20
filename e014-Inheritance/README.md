# Inheritance

- The idea of inheritance is the creation of new classes from another already existing.
- When one class "inherits" another, it inherits its attributes and methods.
- The existing class is called superclass or parent class and the new class is called subclass or daughter class.
- Through inheritance we can add new features, and we can overwrite the inherited ones. Overwriting a method is redefining it in the inherited class.


### To inherit from another class

```
class Car(Vehicle):
```


### Overload of methods

- Using super() to access the methods of the parent class

    ```
    def __init__(self, wheels, weight, brand, trailer):
        super().__init__(wheels, weight, brand)
        self.__trailer = trailer

    def speedUp(self):
        super().speedUp()
        print("Speed up (from the subclass car)")
    ```