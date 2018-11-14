print("########################### 1 ############################")
my_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "keyN": "valueN"
}

print(my_dictionary)
print(my_dictionary["key3"])

"""
Output:
    {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'keyN': 'valueN'}
    value3
"""


print("########################### 2 ############################")
my_dictionary["key3"] = "new value"
my_dictionary["key5"] = "value5"

print(my_dictionary)
print(my_dictionary["key3"])

"""
Output:
    {'key1': 'value1', 'key2': 'value2', 'key3': 'new value', 'key4': 'value4', 'keyN': 'valueN', 'key5': 'value5'}
    new value
"""


print("########################### 3 ############################")
inner_dictionary = {
    "key1": "innerValue",
    2: 5
}

mix_dictionary = {
    "key1": "value1",
    "key2": 2,
    "key3": inner_dictionary
}

print(mix_dictionary)
print(mix_dictionary["key3"])
print(mix_dictionary["key3"][2])

"""
Output:
    {'key1': 'value1', 'key2': 2, 'key3': {'key1': 'innerValue', 2: 5}}
    {'key1': 'innerValue', 2: 5}
    5
"""


print("########################### 4 ############################")
del mix_dictionary["key3"]
# mix_dictionary.pop("key3")
print(mix_dictionary)
mix_dictionary.clear()
print(mix_dictionary)

"""
Output:
    {'key1': 'value1', 'key2': 2}
    {}
"""


print("########################### 5 ############################")
print(len (my_dictionary))
"""
Output:
    6
"""


print("########################### 6 ############################")
print(my_dictionary.keys())
"""
Output:
    dict_keys(['key1', 'key2', 'key3', 'key4', 'keyN', 'key5'])
"""


print("########################### 7 ############################")
print(my_dictionary.values())
"""
Output:
    dict_values(['value1', 'value2', 'new value', 'value4', 'valueN', 'value5'])
"""


print("########################### 8 ############################")
dict = my_dictionary.copy()
print(dict)
"""
Output:
    {'key1': 'value1', 'key2': 'value2', 'key3': 'new value', 'key4': 'value4', 'keyN': 'valueN', 'key5': 'value5'}
"""


print("########################### 9 ############################")
keys = {'a', 'e', 'i', 'o', 'u' }
dict2 = dict.fromkeys(keys)
print(dict2)

value = ["v"]
dict2 = dict.fromkeys(keys, value)
print(dict2)

value.append(2)
print(dict2)
"""
Output:
    {'u': None, 'a': None, 'i': None, 'e': None, 'o': None}
    {'u': ['v'], 'a': ['v'], 'i': ['v'], 'e': ['v'], 'o': ['v']}
    {'u': ['v', 2], 'a': ['v', 2], 'i': ['v', 2], 'e': ['v', 2], 'o': ['v', 2]}
"""


print("########################### 10 ############################")
print(mix_dictionary)
mix_dictionary.update(dict2)
print(mix_dictionary)
"""
Output:
    {}
    {'u': ['v', 2], 'i': ['v', 2], 'e': ['v', 2], 'a': ['v', 2], 'o': ['v', 2]}
"""