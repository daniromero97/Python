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
c.properties()

m = Motorcycle(2, 700, "Honda", False)
m.properties()