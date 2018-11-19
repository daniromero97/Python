print("########################### 1 ############################")
def function_name():
    print("Hello world!!!")

function_name()

""""
output:
    Hello world!!!
"""


print("########################### 2 ############################")
def function_name():
     return "Hello world!!!"

function_return = function_name()
print(function_return)
print(function_name())

""""
output:
    Hello world!!!
    Hello world!!!
"""


print("########################### 3 ############################")
def sum(n, n2, n3):
    return n + n2 + n3

function_return = sum(5, 7, 9)
print(function_return)

""""
output:
    21
"""


print("########################### 4 ############################")
def sum10(num, n=10):
    return num + n

function_return = sum10(5)
print(function_return)

""""
output:
    15
"""


print("########################### 5 ############################")
def sum10(num, n=10):
    return num + n

function_return = sum10(num=15, n=20)
print(function_return)

""""
output:
    35
"""


print("########################### 6 ############################")
def greet(message, *names):
    all_names = ""
    for name in names:
        all_names += " >> %s << " % (name)

    return "%s %s" % (message, all_names)


function_return = greet("Hi", "Dani", "Bea")
print(function_return)

""""
output:
    Hi  >> Dani <<  >> Bea << 
"""


print("########################### 7 ############################")
def greet(message, *names, **kwords):
    all_names = ""
    for name in names:
        all_names += " >> %s << " % (name)

    all_kwords = ""
    for kword in kwords:
        all_kwords += " >> key: %s << " % kwords[kword]

    return "%s %s and keys %s" % (message, all_names, all_kwords)


function_return = greet("Hi", "Dani", "Bea", key1 = "k1", key2 = "k2")
print(function_return)

""""
output:
    Hi  >> Dani <<  >> Bea <<  and keys  >> key: k1 <<  >> key: k2 << 
"""


print("########################### 8 ############################")
def my_function(parameter1, parameter2):
    return "%s --- %s" % (parameter1, parameter2)

function_return = my_function(*["p1", "p2"])
print(function_return)

function_return2 = my_function(**{"parameter1": "p1", "parameter2": "p2"})
print(function_return2)

""""
output:
    p1 --- p2
    p1 --- p2
"""