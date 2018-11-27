import decimal

print("####################### 1 #######################")
print(1/3)
print(decimal.Decimal(1) / decimal.Decimal(3))

"""
output:
    0.3333333333333333
    0.3333333333333333333333333333
"""


print("####################### 2 #######################")
print(0.1 + 0.2)
print(decimal.Decimal(0.1) / decimal.Decimal(0.2))

"""
output:
    0.30000000000000004
    0.5
"""


print("####################### 3 #######################")
print(decimal.Decimal(0.1) + decimal.Decimal(0.2))
print(decimal.Decimal('0.1') + decimal.Decimal('0.2'))

"""
output:
    0.3000000000000000166533453694
    0.3
"""


print("####################### 4 #######################")
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


print("####################### 5 #######################")
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
