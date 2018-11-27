import fractions, decimal

print("##################### 1 #####################")
print(10/18)
print(decimal.Decimal(10) / decimal.Decimal(18))
print(fractions.Fraction(10, 18))

"""
output:
    0.5555555555555556
    0.5555555555555555555555555556
    5/9
"""


print("##################### 2 #####################")
print(fractions.Fraction(324, 18) + fractions.Fraction(324, 7))
print(fractions.Fraction(324, 18) - fractions.Fraction(324, 7))
print(fractions.Fraction(324, 18) * fractions.Fraction(324, 7))
print(fractions.Fraction(324, 18) / fractions.Fraction(324, 7))

"""
output:
    450/7
    -198/7
    5832/7
    7/18
"""


print("##################### 3 #####################")
print(fractions.Fraction(342, 21456))
print(fractions.Fraction(342, 21456).limit_denominator(1000))
print(fractions.Fraction(342, 21456).limit_denominator(100))

"""
output:
    19/1192
    15/941
    1/63
"""


print("##################### 4 #####################")
print(fractions.Fraction(342, 21456))
print(fractions.Fraction(342, 21456).numerator)
print(fractions.Fraction(342, 21456).denominator)

"""
output:
    19/1192
    19
    1192
"""

