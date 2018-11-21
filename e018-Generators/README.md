# Generators

- Generators are invokable objects, such as functions and methods, which implement the "next" method.
- This is usually done using the expression yield.

### Functioning

- They extract the values of a function and store them in iterable objects.
- The values are stored one by one.
- For each call a value is returned, while the generator remains in a paused state.

### Utilities

- More efficient than the functions.
- There will be times when we are interested in having our values returned one by one.

### 'yield' expression

- Returns an object in the local scope.
- Unlike 'return' the function does not end, it continues its execution.


### Examples:

```
def number_generator(number):
    num = 0
    while num<number:
        yield num
        num+=1


numbers = number_generator(5)
print(next(numbers))
print(next(numbers))
print(next(numbers))

"""
output:
    0
    1
    2
"""
```
    
    
```
def number_generator2():
    n = 1
    print('First print')
    yield n

    n += 1
    print('Second print')
    yield n

    n += 1
    print('Third print')
    yield n

    n += 1
    print('Last print')
    yield n


numbers = number_generator2()
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
# print(next(numbers))      # Error StopIteration

"""
output:
    First print
    1
    Second print
    2
    Third print
    3
    Last print
    4
"""   
    
```