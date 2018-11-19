print("########################### 1 ############################")
def greet():
    return "Hello world"

def full_greeting(name):
    return "%s and hello %s" % (greet(), name)

print(full_greeting("Dani"))

""""
output:
    Hello world and hello Dani
"""


print("########################### 2 ############################")
def greet():
    return "Hello world"

def full_greeting(name, function=""):
    return "%s and hello %s" % (globals()[function](), name)

print(full_greeting("Dani", "greet"))

print(locals()["full_greeting"]("Dani", "greet"))

""""
output:
    Hello world and hello Dani
    Hello world and hello Dani
"""


print("########################### 3 ############################")
def greet():
    return "Hello world"

def full_greeting(name, function=""):
    r = "error"
    if function in globals():
        if callable(globals()[function]):
            r = "%s and hello %s" % (globals()[function](), name)
    return r

print(full_greeting("Dani", "greet"))
print(full_greeting("Dani", "greeeeet"))


if "full_greeting" in locals():
    if callable(locals()["full_greeting"]):
        print(locals()["full_greeting"]("Dani", "greet"))


""""
output:
    Hello world and hello Dani
    error
    Hello world and hello Dani
"""


