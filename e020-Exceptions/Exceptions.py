print("##################### 1 #####################")
print("Division")
#print(5/0)
print("End")

"""
output:
    Division
    Traceback (most recent call last):
      File ".../Python/e020-Exceptions/Exceptions.py", line 1, in <module>
        print(5/0)
    ZeroDivisionError: division by zero
"""


print("##################### 2 #####################")
print("Division")

try:
    print(5/0)
except ZeroDivisionError:
    print("It can not divide between zero.")

print("End")

"""
output:
    Division
    It can not divide between zero.
    End
"""


print("##################### 3 #####################")
print("Division")

try:
    print((5/"test"))
    print(5/0)
except ZeroDivisionError:
    print("It can not divide between zero.")
except TypeError:
    print("The division has to be just numbers.")

print("End")

"""
output:
    Division
    The division has to be just numbers.
    End
"""


print("##################### 4 #####################")
print("Division")
"""
try:
    print((5/"test"))
    print(5/0)
finally:
    print("End")
"""
"""
output:
    Division
    The division has to be just numbers.
    End
"""
