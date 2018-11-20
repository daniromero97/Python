class Vehicle(object):
    def __init__(self, wheels, weight, brand):
        self.__wheels = wheels
        self.__weight = weight
        self.__brand = brand

    def properties(self):
        print("Wheels: %d, weight: %d kg, brand: %s" % (self.__wheels, self.__weight, self.__brand))


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


c = Car(4, 1200, "Audi", True)
m = Motorcycle(2, 700, "Honda", False)


print("############## 1 ##############")
print(issubclass(Car, Vehicle))

"""
output:
    True
"""

print("############## 2 ##############")
print(isinstance(c, Vehicle))
print(isinstance(m, Vehicle))
print(isinstance(c, Motorcycle))

"""
output:
    True
    True
    False
"""


print("############## 3 ##############")
print(dir(c))

"""
output:
    ['_Car__trailer', '_Vehicle__brand', '_Vehicle__weight', '_Vehicle__wheels', '__class__', '__delattr__', 
    '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
    '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
    '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'properties']
"""


print("############## 4 ##############")
print(vars(c))

"""
output:
    {'_Vehicle__wheels': 4, '_Vehicle__weight': 1200, '_Vehicle__brand': 'Audi', '_Car__trailer': True}
"""


print("############## 5 ##############")
print(getattr(c, '_Vehicle__brand', 'None'))

"""
output:
    Audi
"""


print("############## 6 ##############")
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


print("############## 7 ##############")
print(delattr(c, 'name'))
print(getattr(c, 'name', 'None'))

"""
output:
    None
    None
"""