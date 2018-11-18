print("########################### 1 ############################")
a,b = "Message", "Hello world!!"
print("%s = %s" % (a, b))

"""
Output:
    Message = Hello world!!
"""


print("########################### 2 ############################")
a,b = "Message", "Hello world!!"
print(a + "=" + b)

"""
Output:
    Message = Hello world!!
"""


print("########################### 3 ############################")
"""
a,b = "Value", 3
print(a + "=" + b)


Output:
    Traceback (most recent call last):
      File ".../Python/e007-Format/Format.py", line 2, in <module>
        print(a + "=" + b)
    TypeError: can only concatenate str (not "int") to str
"""


print("########################### 4 ############################")
a,b = "Value", 3
print("%s = %d" % (a, b))

"""
Output:
    Value = 3
"""


print("########################### 5 ############################")
a = 3
print("Value = %d" % (a,))

"""
Output:
    Value = 3
"""


print("########################### 6 ############################")
a = 3.5678
print("Value = %d" % (a,))
print("Value = %f" % (a,))
print("Value = %.2f" % (a,))

"""
Output:
    Value = 3
    Value = 3.567800
    Value = 3.57
"""