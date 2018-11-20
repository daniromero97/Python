class Vehicle(object):
    def __init__(self, wheels, weight, brand):
        self.__wheels = wheels
        self.__weight = weight
        self.__brand = brand

    def properties(self):
        print("Wheels: %d, weight: %d kg, brand: %s" % (self.__wheels, self.__weight, self.__brand))

    def speedUp(self):
        print("Speed up (from the parent class)")


class Car(Vehicle):

    def __init__(self, wheels, weight, brand, trailer):
        super().__init__(wheels, weight, brand)
        self.__trailer = trailer

    def speedUp(self):
        super().speedUp()
        print("Speed up (from the subclass car)")


c1 = Car(4, 1200, "Audi", True)
c1.properties()
c1.speedUp()
