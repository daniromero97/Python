# math module

- It provides access to the mathematical functions defined by the C standard.
- For complex numbers use the cmath module.

### Constants

##### pi and e

- (pi) The mathematical constant π = 3.141592…, to available precision.
- (e) The mathematical constant e = 2.718281…, to available precision.

```
print(math.pi)
print(math.e)

"""
output:
    3.141592653589793
    2.718281828459045
"""
```


### Angular conversion

##### degrees() and radians()

- (degrees) Convert angle x from radians to degrees.
- (radians) Convert angle x from degrees to radians.

```
print(math.degrees(1))
print(math.radians(114.6))

"""
output:
    57.29577951308232
    2.0001473227855016
"""
```


### Number-theoretic and representation functions

##### ceil()

- Returns the smallest integer greater than or equal to a given number.

```
print(math.ceil(3.4))
print(math.ceil(3.5))
print(math.ceil(-3.4))
print(math.ceil(-3.5))

"""
output:
    4
    4
    -3
    -3
"""
```

##### floor()

- Returns the smallest integer less than or equal to a given number.

```
print(math.floor(3.4))
print(math.floor(3.5))
print(math.floor(-3.4))
print(math.floor(-3.5))

"""
output:
    3
    3
    -4
    -4
"""
```

##### trunc()

- Returns a truncated value to an integer.

```
print(math.trunc(3.4))
print(math.trunc(3.5))
print(math.trunc(-3.4))
print(math.trunc(-3.5))

"""
output:
    3
    3
    -3
    -3
"""
```

##### fabs()

- Returns the absolute value of a number.

```
print(math.fabs(-2.4))
print(math.fabs(2.4))

"""
output:
    2.4
    2.4
"""
```

##### factorial()

- Return the factorial of a number. Raises ValueError if the value is not integer or is negative.

```
print(math.factorial(2))
print(math.factorial(3))
print(math.factorial(4))
print(math.factorial(5))

"""
output:
    2
    6
    24
    120
"""
```

##### fmod()

- Return the rest of a whole division.

```
print(math.fmod(5,2))
print(math.fmod(10,3))
print(math.fmod(15,4))

"""
output:
    1.0
    1.0
    3.0
"""
```


### Power and logarithmic functions

##### exp()

- Return e raised to the power of a value, where e = 2.718281… is the base of natural logarithms. This is usually more accurate than math.e ** x or pow(math.e, x).

```
print(math.exp(1))
print(math.exp(2))
print(math.exp(3))
print(math.exp(4))

"""
output:
    2.718281828459045
    7.38905609893065
    20.085536923187668
    54.598150033144236
"""
```

##### log()

- With one argument, return the natural logarithm of a value (to base e).
- With two arguments, return the logarithm of a value to the given base, calculated as log(x)/log(base).

```
print(math.log(1))
print(math.log(2))
print(math.log(3))
print(math.log(1, 10))
print(math.log(2, 10))
print(math.log(3, 10))

"""
output:
    0.0
    0.6931471805599453
    1.0986122886681098
    0.0
    0.30102999566398114
    0.47712125471966244
"""
```

##### log1p()

- Return the natural logarithm of 1+x (base e). The result is calculated in a way which is accurate for x near zero.

```
print(math.log1p(1))
print(math.log1p(2))
print(math.log1p(3))

"""
output:
    0.6931471805599453
    1.0986122886681096
    1.3862943611198906
"""
```

##### log10()

- Return the base-10 logarithm of a value. This is usually more accurate than log(x, 10).

```
print(math.log10(1))
print(math.log10(2))
print(math.log10(3))

"""
output:
    0.0
    0.3010299956639812
    0.47712125471966244
"""
```

##### pow()

- Raise the base of a first value to the exponent of a second value.

```
print(math.pow(2, 2))
print(math.pow(2, 3))
print(math.pow(2, 4))

"""
output:
    4.0
    8.0
    16.0
"""
```

##### sqrt()

- Returns the square root of a value.

```
print(math.sqrt(25))
print(math.sqrt(100))
print(math.sqrt(144))

"""
output:
    5.0
    10.0
    12.0
"""
```

##### hypot()

- Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y).

```
print(math.hypot(10, 5))
print(math.hypot(20, 5))
print(math.hypot(30, 5))

"""
output:
    11.180339887498949
    20.615528128088304
    30.4138126514911
"""
```


### Trigonometric functions

##### acos()

- Return the arc cosine of a value, in radians.

```
print(math.acos(0.1))
print(math.acos(0.2))
print(math.acos(0.3))

"""
output:
    1.4706289056333368
    1.369438406004566
    1.2661036727794992
"""
```

##### asin()

- Return the arc sine of a value, in radians.

```
print(math.asin(0.1))
print(math.asin(0.2))
print(math.asin(0.3))

"""
output:
    0.1001674211615598
    0.2013579207903308
    0.3046926540153975
"""
```

##### atan()

- Return the arc tangent of a value, in radians.

```
print(math.atan(0.1))
print(math.atan(0.2))
print(math.atan(0.3))

"""
output:
    0.09966865249116204
    0.19739555984988078
    0.2914567944778671
"""
```

##### cos()

- Return the cosine of a value, in radians.

```
print(math.cos(45))
print(math.cos(90))
print(math.cos(180))

"""
output:
    5.0
    10.0
    12.0
"""
```

##### sin()

- Return the sine of a value, in radians.

```
print(math.sin(45))
print(math.sin(90))
print(math.sin(180))

"""
output:
    5.0
    10.0
    12.0
"""
```

##### tan()

- Return the tangent of a value, in radians.

```
print(math.tan(45))
print(math.tan(90))
print(math.tan(180))

"""
output:
    5.0
    10.0
    12.0
"""
```


### Hyperbolic functions

##### acosh()

- Return the inverse hyperbolic cosine of a value.

```
print(math.acosh(45))
print(math.acosh(90))
print(math.acosh(180))

"""
output:
    5.0
    10.0
    12.0
"""
```

##### asinh()

- Return the inverse hyperbolic sine of a value.

```
print(math.asinh(45))
print(math.asinh(90))
print(math.asinh(180))

"""
output:
    5.0
    10.0
    12.0
"""
```

##### atanh()

- Return the inverse hyperbolic tangent of a value.

```
print(math.atanh(0.1))
print(math.atanh(0.2))
print(math.atanh(0.3))

"""
output:
    0.10033534773107558
    0.2027325540540822
    0.30951960420311175
"""
```

##### cosh()

- Return the hyperbolic cosine of a value.

```
print(math.cosh(0.1))
print(math.cosh(0.2))
print(math.cosh(0.3))

"""
output:
    1.0050041680558035
    1.020066755619076
    1.0453385141288605
"""
```

##### sinh()

- Return the hyperbolic sine of a value.

```
print(math.sinh(0.1))
print(math.sinh(0.2))
print(math.sinh(0.3))

"""
output:
    0.10016675001984403
    0.20133600254109402
    0.3045202934471426
"""
```

##### tanh()

- Return the hyperbolic tangent of a value.

```
print(math.tanh(0.1))
print(math.tanh(0.2))
print(math.tanh(0.3))

"""
output:
    0.09966799462495582
    0.197375320224904
    0.2913126124515909
"""
```










