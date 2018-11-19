print("########################### 1 ############################")
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


print("########################### 2 ############################")
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



