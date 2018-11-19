class Person(object):
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        print("Person created >>> name: %s, height: %.2f m, weight: %.1f kg, age: %d years old" % (self.name, self.height, self.weight, self.age))

    def eat(self):
        print("%s is eating" % self.name)

    def drink(self):
        print("%s is drinking" % self.name)

    def sleep(self):
        print("%s is sleeping" % self.name)


p1 = Person("Gonzalo", 1.78, 74, 25)
p1.eat()
p1.drink()
p1.sleep()




