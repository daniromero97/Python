print("########################### 1 ############################")
a, b, c = 'value', 2, False
print(a)
print(b)
print(c)

"""
Output:
    value
    2
    False
"""


print("########################### 2 ############################")
a, b = 5, 10

if a>b:
    print("'a' greater than 'b'")

if a<b:
    print("'a' smaller than 'b'")

"""
Output:
    'a' smaller than 'b'
"""


print("########################### 3 ############################")
if a>b:
    print("'a' greater than 'b'")
else:
    print("'a' smaller than 'b'")

"""
Output:
    'a' smaller than 'b'
"""


print("########################### 4 ############################")
a, b, c = 2, 3, 4

if a>b and a>c:
    print("'a' is the biggest")
elif b>a and b>c:
    print("'b' is the biggest")
else:
    print("'c' is the biggest")

"""
Output:
    'c' is the biggest
"""