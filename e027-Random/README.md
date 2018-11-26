# Random

- Using the random module of the Python standard library we can obtain random data.

##### random()

- Returns a random number between 0 and 1, not including 1.

```
print(random.random() * 10)
print(random.random() * 10)
print(random.random() * 10)

"""
output:
    4.305160020840581
    7.416683390248872
    0.5282572515936235
"""
```

##### randint()

- Returns an integer random number between two.

```
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))

"""
output:
    9
    3
    7
"""
```

##### randrange()

- Returns a randomly selected item from the range (start, stop, step).

```
print(random.randrange(0, 21, 2))
print(random.randrange(0, 21, 2))
print(random.randrange(0, 21, 2))

"""
output:
    20
    12
    10
"""
```

##### choice()

- Returns any random data of a given sequence.

```
my_list = [15, True, "test", 30, False]
print(random.choice(my_list))
print(random.choice(my_list))
print(random.choice(my_list))

"""
output:
    True
    15
    False
"""
```

##### shuffle()

- Returns a mixture of the elements of a given sequence.

```
my_list = [15, True, "test", 30, False]
print(my_list)
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)

"""
output:
    [15, True, 'test', 30, False]
    ['test', 15, True, False, 30]
    [False, 30, 15, True, 'test']
"""
```

##### sample()

- Returns n random elements of a given sequence.

```
my_list = [15, True, "test", 30, False]
print(random.sample(my_list, 2))
print(random.sample(my_list, 3))
print(random.sample(my_list, 4))

"""
output:
    ['test', 15]
    [False, 15, 'test']
    [30, 'test', 15, False]
"""
```


##### seed()

- Fixed by a "seed" the same start in each sequence, thus allowing to obtain series with the same values.

```
random.seed(10)
print(random.randint(10, 20))
print(random.randint(10, 20))
random.seed(10)
print(random.randint(10, 20))
print(random.randint(10, 20))
random.seed(10)
print(random.randint(10, 20))
print(random.randint(10, 20))

"""
output:
    19
    10
    19
    10
    19
    10
"""
```
