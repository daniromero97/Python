class Vehicle(object):
    def __init__(self, wheels, weight, brand):
        self.__wheels = wheels
        self.__weight = weight
        self.__brand = brand
        self.__autonomy = 200

    def properties(self):
        print("Wheels: %d, weight: %d kg, brand: %s, charge %d" % (self.__wheels, self.__weight, self.__brand, self.__autonomy))

    def speedUp(self):
        print("Speed up (from the parent class)")
        self.__autonomy -= 5

    def charge(self):
        if(self.__autonomy<300):
            self.__autonomy += 30
            print("Loaded")
        else:
            print("Maximum load")


class ElectricVehicle(object):
    def electric_charge(self):
        print("Electric charge")


class Car(Vehicle, ElectricVehicle):

    def __init__(self, wheels, weight, brand, trailer):
        super().__init__(wheels, weight, brand)
        self.__trailer = trailer

    def speedUp(self):
        super().speedUp()
        print("Speed up (from the subclass car)")


c1 = Car(4, 1200, "Audi", True)
c1.properties()
c1.speedUp()
c1.charge()
c1.electric_charge()
c1.properties()
