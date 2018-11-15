print("########################### 1 ############################")
my_list = ["value 1", "value 2", "value 3", ["value 4.1", "value 4.2"], 5]

print(my_list)
print(my_list[0])
print(my_list[3])
print(my_list[3][0])
print(my_list[4])

"""
Output:
    ['value 1', 'value 2', 'value 3', ['value 4.1', 'value 4.2'], 5]
    value 1
    ['value 4.1', 'value 4.2']
    value 4.1
    5
"""


print("########################### 2 ############################")
print(len(my_list))
print(my_list[-3])
print(my_list[2])

"""
Output:
    5
    value 3
    value 3
"""


print("########################### 3 ############################")
print(my_list[0:3])
print(my_list[2:3])
print(my_list[-3:-1])

"""
Output:
    ['value 1', 'value 2', 'value 3']
    ['value 3']
    ['value 3', ['value 4.1', 'value 4.2']]
"""


print("########################### 4 ############################")
print(my_list[0:3])
print(my_list[:3])

print(my_list[3:5])
print(my_list[3:])

print(my_list)
print(my_list[:])

"""
Output:
    ['value 1', 'value 2', 'value 3']
    ['value 1', 'value 2', 'value 3']
    [['value 4.1', 'value 4.2'], 5]
    [['value 4.1', 'value 4.2'], 5]
    ['value 1', 'value 2', 'value 3', ['value 4.1', 'value 4.2'], 5]
    ['value 1', 'value 2', 'value 3', ['value 4.1', 'value 4.2'], 5]
"""


print("########################### 5 ############################")
empty_list = []
print(empty_list)
empty_list.append([1, 2])
print(empty_list)
print(len(empty_list))

"""
Output:
    []
    [[1, 2]]
    1
"""

print("########################### 6 ############################")
empty_list = []
print(empty_list)
empty_list.extend([1, 2])
print(empty_list)
print(len(empty_list))

"""
Output:
    []
    [1, 2]
    2
"""

print("########################### 7 ############################")
print(empty_list)
empty_list.insert(1, "new value")
print(empty_list)
print(len(empty_list))

empty_list.insert(1, [1, 2])
print(empty_list)
print(len(empty_list))

"""
Output:
    [1, 2]
    [1, 'new value', 2]
    3
    [1, [1, 2], 'new value', 2]
    4
"""


print("########################### 8 ############################")
my_remove_list = ["a", "b", "a", "b", "a", "b"]
print(my_remove_list)
my_remove_list.remove("a")
print(my_remove_list)

"""
Output:
    ['a', 'b', 'a', 'b', 'a', 'b']
    ['b', 'a', 'b', 'a', 'b']
"""


print("########################### 9 ############################")
print(my_remove_list)
del my_remove_list[0]
print(my_remove_list)
del my_remove_list[0:3]
print(my_remove_list)
del my_remove_list[:]
print(my_remove_list)

"""
Output:
    ['b', 'a', 'b', 'a', 'b']
    ['a', 'b', 'a', 'b']
    ['b']
    []
"""


print("########################### 10 ############################")
my_remove_list = ["a", "b", "c", "a", "b", "c"]
print(my_remove_list)
my_remove_list.pop()
print(my_remove_list)
my_remove_list.pop(2)
print(my_remove_list)

"""
Output:
    ['a', 'b', 'c', 'a', 'b', 'c']
    ['a', 'b', 'c', 'a', 'b']
    ['a', 'b', 'a', 'b']
"""


print("########################### 11 ############################")
print(my_remove_list)
print(my_remove_list.index("a"))
print(my_remove_list.index("b"))

"""
Output:
    ['a', 'b', 'a', 'b']
    0
    1
"""


print("########################### 12 ############################")
print(my_remove_list)
print("a" in my_remove_list)
print("c" in my_remove_list)

"""
Output:
    ['a', 'b', 'a', 'b']
    True
    False
"""

print("########################### 13 ############################")
list = [1, 2]
print(list)

other_list = [3, 4]
list = list + other_list
print(list)

list += [5, 6]
print(list)

#list = list * 2
list *= 2
print(list)

"""
Output:
    [1, 2]
    [1, 2, 3, 4]
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
"""


print("########################### 14 ############################")
list = [1, 1, 1, 1, 2, 2, 3]
print(list)
print(list.count(1))
print(list.count(2))
print(list.count(3))

"""
Output:
    [1, 1, 1, 2, 2, 3]
    4
    2
    1
"""


print("########################### 15 ############################")
list = [1, 4, 2, 8, 10, 2]
print(list)

list.sort()
print(list)

"""
Output:
    [1, 4, 2, 8, 10, 2]
    [1, 2, 2, 4, 8, 10]
"""


print("########################### 16 ############################")
list = [1, 5, 8, 2]
print(list)

list.reverse()
print(list)

"""
Output:
    [1, 5, 8, 2]
    [2, 8, 5, 1]
"""


print("########################### 17 ############################")
print(list)
print(min(list))
print(max(list))

"""
Output:
    [2, 8, 5, 1]
    1
    8
"""


print("########################### 18 ############################")
print(list)
list.clear()
print(list)

"""
Output:
    [2, 8, 5, 1]
    []
"""