import ExternalModule as exMod
from my_package.myModule2 import age as a1
from my_package.myModule3 import age as a2

print(exMod.age)
print(a1)
print(a2)

"""
output:
    21
    22
    23
"""