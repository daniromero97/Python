print("####################### 1 #######################")
my_first_variable = 32
MY_FIRST_CONSTANT = 3.1416
my_string = "Hello World!"

print(my_first_variable)
print(MY_FIRST_CONSTANT)
print(my_string)


print("####################### 2 #######################")
my_first_variable = 35
MY_FIRST_CONSTANT = 3.15
my_string = "Hello World!!!!!!"

print(my_first_variable)
print(MY_FIRST_CONSTANT)
print(my_string)


print("####################### 3 #######################")
my_first_variable = my_first_variable + 5
MY_FIRST_CONSTANT = MY_FIRST_CONSTANT / 2
my_string = my_string * 3

print(my_first_variable)
print(MY_FIRST_CONSTANT)
print(my_string)


print("####################### 4 #######################")
a, b, c, d = 10, False, "Hello", "2"
print(a)
print(b)
print(c)
print(d)
print("-----------------------")
print(d+"5")    # string


print("####################### 5 #######################")
# Data entry by console
# Python 3
print("Write your name: ")
name = input()
print(f"Your name is: {name}")
print(type(name))       # type() returns the data type of the variable

print("-----------------------")
print("Write your age: ")
age = input()
print(f"Your age is: {age}")
print(type(age))
age = int(age)      # With int() we casted the data to numeric type
print(type(age))