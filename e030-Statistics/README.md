# Statistics

### Averages and measures of central location

- These functions calculate an average or typical value from a population or sample.

##### mean()

- Arithmetic mean (“average”) of data.

```
print(statistics.mean([1,2,3,4,5,6]))
print(statistics.mean([2,2,3,3,4,4]))

"""
output:
    3.5
    3
"""
```

##### harmonic_mean()

- Harmonic mean of data.

```
print(statistics.harmonic_mean([1,2,3,4,5,6]))
print(statistics.harmonic_mean([2,2,3,3,4,4]))

"""
output:
    2.4489795918367347
    2.769230769230769
"""
```

##### median()

- Median (middle value) of data.

```
print(statistics.median([1,2,3,4,5,6]))
print(statistics.median([2,2,3,3,4,4]))

"""
output:
    3.5
    3
"""
```

##### median_low()

- Low median of data.

```
print(statistics.median_low([1,2,3,4,5,6]))
print(statistics.median_low([2,2,3,3,4,4]))

"""
output:
    3
    3
"""
```

##### median_high()

- High median of data.

```
print(statistics.median_high([1,2,3,4,5,6]))
print(statistics.median_high([2,2,3,3,4,4]))

"""
output:
    4
    3
"""
```

##### median_grouped()

- Median, or 50th percentile, of grouped data. 

```
print(statistics.median_grouped([1,2,3,4,5,6]))
print(statistics.median_grouped([1,2,2,3,4,4,4,4,4,5]))

"""
output:
    3.5
    3.7
"""
```

##### mode()

- Mode (most common value) of discrete data.

```
print(statistics.mode([1,2,2,3]))
print(statistics.mode([1,2,2,3,3,3]))

"""
output:
    2
    3
"""
```


### Measures of spread

- These functions calculate a measure of how much the population or sample tends to deviate from the typical or average values.

##### pstdev()

- Population standard deviation of data.

```
print(statistics.pstdev([1,2,3,4,5,6]))
print(statistics.pstdev([2,2,3,3,4,4]))

"""
output:
    1.707825127659933
    0.816496580927726
"""
```

##### pvariance()

- Population variance of data.

```
print(statistics.pvariance([1,2,3,4,5,6]))
print(statistics.pvariance([2,2,3,3,4,4]))

"""
output:
    2.9166666666666665
    0.6666666666666666
"""
```

##### stdev()

- Sample standard deviation of data.

```
print(statistics.stdev([1,2,3,4,5,6]))
print(statistics.stdev([2,2,3,3,4,4]))

"""
output:
    1.8708286933869707
    0.8944271909999159
"""
```

##### variance()

- Sample variance of data.

```
print(statistics.variance([1,2,3,4,5,6]))
print(statistics.variance([2,2,3,3,4,4]))

"""
output:
    3.5
    0.8
"""
```
