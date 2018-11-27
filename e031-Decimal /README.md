# Decimal

- Even the most basic mathematical operations can sometimes give the wrong result. This happens due to limitations in storing the exact value of some numbers.
- Decimal numbers are much more accurate than floating numbers.
    
    ```
    print(1/3)
    print(decimal.Decimal(1) / decimal.Decimal(3))
    
    """
    output:
        0.3333333333333333
        0.3333333333333333333333333333
    """
    ```
    
- If you think that it is not necessary so much precision try the following:
    
    ```
    print(0.1 + 0.2)
    print(decimal.Decimal(0.1) / decimal.Decimal(0.2))
    
    """
    output:
        0.30000000000000004
        0.5
    """
    ```

- To get accurate results like the ones we are in, we need something that supports fast and correctly rounded floating-point decimal arithmetic.

    ```
    print(decimal.Decimal(0.1) + decimal.Decimal(0.2))
    print(decimal.Decimal('0.1') + decimal.Decimal('0.2'))
    
    """
    output:
        0.3000000000000000166533453694
        0.3
    """
    ```


### prec

- To control the decimal precision.

```
print(decimal.Decimal(0.1) + decimal.Decimal(0.2))

decimal.getcontext().prec = decimal.getcontext().capitals
print(decimal.Decimal(0.1) + decimal.Decimal(0.2))

decimal.getcontext().prec = 5
print(decimal.Decimal(0.1) + decimal.Decimal(0.2))

decimal.getcontext().prec = decimal.getcontext().Emax
print(decimal.Decimal(0.1) + decimal.Decimal(0.2))

"""
output:
    0.3000000000000000166533453694
    0.3
    0.30000
    0.3000000000000000166533453693773481063544750213623046875
"""
```


### rounding

```
decimal.getcontext().prec = 3
decimal.getcontext().rounding = decimal.ROUND_DOWN
print(decimal.Decimal(0.1234) + decimal.Decimal(0.2))

decimal.getcontext().rounding = decimal.ROUND_CEILING
print(decimal.Decimal(0.1234) + decimal.Decimal(0.2))

"""
output:
    0.323
    0.324
"""
```

- Oficial documentation: https://docs.python.org/3/library/decimal.html








