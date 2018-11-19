# Recursion

- Recursive functions are functions that call themselves.
- They should be used in specific cases since it is easy to fall into an infinite iteration.

#### Example calculate the factorial of a number

```
def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return 1

n = 0
while(n<=6):
    print("##########\n%s" % factorial(n))
    n+=1

""""
output:
    ##########
    1
    ##########
    1
    ##########
    2
    ##########
    6
    ##########
    24
    ##########
    120
    ##########
    720
"""
```

#### Example calculate the factorial of a number
```
def fibonacci(n):
    if(n<2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 0
while(n<=6):
    print("##########\n%s" % fibonacci(n))
    n+=1

""""
output:
    ##########
    1
    ##########
    1
    ##########
    2
    ##########
    3
    ##########
    5
    ##########
    8
    ##########
    13
"""
```

    