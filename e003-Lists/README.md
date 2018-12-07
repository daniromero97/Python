## Lists

- A list in python is a collection of objects (the values can be of any type of data).
- A list is modifiable, so you can add and remove objects.
- Each item is automatically listed from 0.
    
    ```
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
    ```


- <strong> Negative indexes </strong>
    
    - A negative index accesses the elements from the end of the list counting backwards. The last element of any list that is not empty is always my_list [-1].
    - If you get confused, think about this:
    
    ```
    my_list[-n] == my_list[len(my_list) - n]
    my_list[-3] == my_list[5 - 3]
    ```
    
    ```
    print(len(my_list))
    print(my_list[-3])
    print(my_list[2])
    
    """
    Output:
        5
        value 3
        value 3
    """
    ```
    
    
- <strong> Slicing </strong>

    - A slice is a subset of a list.
    - The return value is all the elements, in order, starting by the first index of the slice, up to the second index without including it.
    - The lists start at zero, so my_list[0:3] returns the first three elements of the list, from li[0] to li[3] (not included).
    
    ```
    print(my_list[0:3])
    print(my_list[2:3])
    print(my_list[-3:-1])
    
    """
    Output:
        ['value 1', 'value 2', 'value 3']
        ['value 3']
        ['value 3', ['value 4.1', 'value 4.2']]
    """
    ```  
    
    
- <strong> Shortcuts </strong>

    - If the first index is 0, you can omit it because it is implicit. That is, my_list[:3] is the same as my_list[0:3].
    - If the last index is the length of the list, you can also omit it. That is, my_list[3:] is the same as my_list[3:5] (keeping in mind that our list has 5 elements).
    - Be careful, my_list[:n] will return the first n elements, and my_list[n:] will return the rest of the elements, regardless of the size of the list.
    - If both indexes are omitted we obtain all the elements, the difference of my_list and my_list[:] is each subset returns a new list, so my_list[:] is a copy of my_list.
        
    ```
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
    ```


        
#### Add items

- <strong> append(values) </strong>
    
    - Add a single element to the end of the list.
    
    ```
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
    ```
    
- <strong> extend(values) </strong>
    
    - Concatenate lists, so if we have an empty list "empty_list = []" and we concatenate it with two elements "empty_list.extend([1, 2])", now our list has two elements.
    - Whereas if we insert "empty_list.append([1, 2])", our list will have a single element.
    
    ```
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
    ```
    
- <strong> insert(index, values) </strong>
    
    - Inserts a single item in a list in a certain position.
    
    ```
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
    ```        


    
#### Delete items

- <strong> remove(value) </strong>
    
    - It eliminates the FIRST appearance of a value in a list, so if it appears twice it will only eliminate the first value.
    
    ```
    my_remove_list = ["a", "b", "a", "b", "a", "b"]
    print(my_remove_list)
    my_remove_list.remove("a")
    print(my_remove_list)
    
    """
    Output:
        ['a', 'b', 'a', 'b', 'a', 'b']
        ['b', 'a', 'b', 'a', 'b']
    """
    ```
    
- <strong> del </strong>
    
    - Remove an item in a certain position.
    
    ```
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
    ```
    
- <strong> pop() </strong>
    
    - Remove the last item from the list and return it.
    - You can also indicate an index.
    
    ```
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
    ```   


    
#### Search items

- <strong> index(value) </strong>
    
    - Find the FIRST appearance of a value and return its index.
    
    ```
    print(my_remove_list)
    print(my_remove_list.index("a"))
    print(my_remove_list.index("b"))
    
    """
    Output:
        ['a', 'b', 'a', 'b']
        0
        1
    """
    ```    
    
 - <strong> in </strong>
    
    - Returns true or false depending on whether the item is in the list.
    
    ```
    print(my_remove_list)
    print("a" in my_remove_list)
    print("c" in my_remove_list)
    
    """
    Output:
        ['a', 'b', 'a', 'b']
        True
        False
    """
    ```  
    
    
    
#### List operators

 - You can use the "+" operator to concatenate elements to a list, it is similar to ".extends (values)" but when concatenating with "+" we get a new list, for this reason "extends" is faster.
 - You can also use the "+ =" operator equivalent to extend.
 - Another operator would be "*".
 
 ```
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
 ``` 
 
 
 
#### Other functionalities

- <strong> count(value) </strong>
    
    - Count how many times a value.
    
    ```
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
    ```
    
- <strong> sort() </strong>
    
    - Sort the list.
    
    ```
    list = [1, 4, 2, 8, 10, 2]
    print(list)
    
    list.sort()
    print(list)
    
    """
    Output:
        [1, 4, 2, 8, 10, 2]
        [1, 2, 2, 4, 8, 10]
    """
    ```
    
- <strong> reverse() </strong>
    
    - Invert the list.
    
    ```
    list = [1, 5, 8, 2]
    print(list)
    
    list.reverse()
    print(list)
    
    """
    Output:
        [1, 5, 8, 2]
        [2, 8, 5, 1]
    """
    ```
    
- <strong> min(list) and max(list) </strong>
    
    - They return the minimum and maximum values.
    
    ```
    print(list)
    print(min(list))
    print(max(list))
    
    """
    Output:
        [2, 8, 5, 1]
        1
        8
    """
    ``` 
    
- <strong> clear() </strong>
    
    - Empty the list
    
    ```
    print(list)
    list.clear()
    print(list)
    
    """
    Output:
        [2, 8, 5, 1]
        []
    """
    ```  
    
    
 