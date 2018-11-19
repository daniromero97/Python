class Person(object):
    def __init__(self, name, height, weight, age):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age

    def properties(self):
        print("Name: %s, height: %.2f m, weight: %.1f kg, age: %d years old" % (self.__name, self.__height, self.__weight, self.__age))

    def eat(self):
        print("%s is eating" % self.__name)

    def drink(self):
        print("%s is drinking" % self.__name)

    def sleep(self):
        print("%s is sleeping" % self.__name)




p1 = Person("Gonzalo", 1.78, 74, 25)
p1.properties()

p1.__name = "Luis"
p1.properties()
print(p1.__name)    # Unresolved attribute reference '__name' for class 'Person'




