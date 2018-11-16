print("########################### 1 ############################")
my_tuple = ("value 1", "value 2", "value 3", ["value 4.1", "value 4.2"], 5, ("value 6.1", "value 6.2"))

print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[2:5])

"""
Output:
    ('value 1', 'value 2', 'value 3', ['value 4.1', 'value 4.2'], 5, ('value 6.1', 'value 6.2'))
    value 1
    ('value 6.1', 'value 6.2')
    ('value 3', ['value 4.1', 'value 4.2'], 5)
"""


print("########################### 2 ############################")
print(my_tuple.index("value 2"))
print(5 in my_tuple)

"""
Output:
    1
    True
"""


print("########################### 3 ############################")
print(len(my_tuple))
print(my_tuple.count("value 3"))

"""
Output:
    6
    1
"""


print("########################### 4 ############################")
my_tuple2 = (1, 4, 5, 21, 2)
print(min(my_tuple2))
print(max(my_tuple2))

"""
Output:
    1
    21
"""


print("########################### 5 ############################")
print(my_tuple)
l = list (my_tuple)
print(l)
t = tuple (l)
print(t)

"""
Output:
    ('value 1', 'value 2', 'value 3', ['value 4.1', 'value 4.2'], 5, ('value 6.1', 'value 6.2'))
    ['value 1', 'value 2', 'value 3', ['value 4.1', 'value 4.2'], 5, ('value 6.1', 'value 6.2')]
    ('value 1', 'value 2', 'value 3', ['value 4.1', 'value 4.2'], 5, ('value 6.1', 'value 6.2'))
"""