## Dictionaries

- Data type that allows you to store an unordered set of key-value pairs, being the UNIQUE keys within the same dictionary, so there can not be two elements with the same key.
- Keys distinguish uppercase.
    
    ```
    my_dictionary = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
        "key4": "value4",
        "keyN": "valueN"
    }
    
    print(my_dictionary)
    print(my_dictionary['key3'])
    
    """
    Output:
        {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'keyN': 'valueN'}
        value3
    """
    ```


#### Add key-value pairs and modify them.

- The syntax for adding pairs is the same as for modifying values.-
- You can not have duplicate keys in a dictionary, assigning a new value to an existing key will eliminate the old value.

    ```
    my_dictionary["key3"] = "new value"
    my_dictionary["key5"] = "value5"
    
    print(my_dictionary)
    print(my_dictionary["key3"])
    
    """
    Output:
        {'key1': 'value1', 'key2': 'value2', 'key3': 'new value', 'key4': 'value4', 'keyN': 'valueN', 'key5': 'value5'}
        new value
    """
    ```

    
#### Mix of data types

- The values can be of any type of data, for example, strings, integers, objects or other dictionaries.
- The keys are more restricted, but they can be for example strings and integers.
- You can also mix the types of keys within a dictionary.

    ```
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
    ```


#### Functionalities

- <strong> del and pop(key) </strong>
    
    - allows you to delete individual elements of a dictionary by its key.
    
    ```
    print(mix_dictionary)
    del mix_dictionary["key3"]
    # mix_dictionary.pop("key3")
    print(mix_dictionary)
    
    """
    Output:
        {'key1': 'value1', 'key2': 2, 'key3': {'key1': 'innerValue', 2: 5}}
        {'key1': 'value1', 'key2': 2}
    """
    ```
    
    
    
- <strong> clear() </strong>
    
    - removes all elements of a dictionary.   
 
    ```
    print(mix_dictionary)
    mix_dictionary.clear()
    print(mix_dictionary)
    
    """
    Output:
        {'key1': 'value1', 'key2': 2}
        {}
    """
    ```



- <strong> len </strong> 
    
    - Returns the number of elements that the dictionary has
    
    ```
    print(len (my_dictionary))
    """
    Output:
        6
    """
    ```


- <strong> keys() </strong>
    
    - Returns a list with dictionary keys
    
    ```
    print(my_dictionary.keys())
    """
    Output:
        dict_keys(['key1', 'key2', 'key3', 'key4', 'keyN', 'key5'])
    """
    ```


- <strong> values() </strong> 
    
    - Returns a list with dictionary values
    
    ```
    print(my_dictionary.values())
    """
    Output:
        dict_values(['value1', 'value2', 'new value', 'value4', 'valueN', 'value5'])
    """
    ```
    
    
- <strong> copy() </strong>
   
    - Returns the copy of a dictionary
    ```
    dict = my_dictionary.copy()
    print(dict)
    """
    Output:
        {'key1': 'value1', 'key2': 'value2', 'key3': 'new value', 'key4': 'value4', 'keyN': 'valueN', 'key5': 'value5'}
    """
    ```


- <strong> fromkeys(list, defaultValue) </strong>
    
    - Create a new dictionary by putting the ones in the list as keys and the default values if you miss them
    ```
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
    ```


- <strong> update(dict2) </strong>
    
    - Add elements from one dictionary to another
    ```
    print(mix_dictionary)
    mix_dictionary.update(dict2)
    print(mix_dictionary)
    """
    Output:
        {}
        {'u': ['v', 2], 'i': ['v', 2], 'e': ['v', 2], 'a': ['v', 2], 'o': ['v', 2]}
    """
    ```