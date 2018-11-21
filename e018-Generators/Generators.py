print("#################### 1 ####################")
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


print("#################### 2 ####################")
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