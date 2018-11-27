import statistics

print("################### 1 ###################")
print(statistics.mean([1,2,3,4,5,6]))
print(statistics.mean([2,2,3,3,4,4]))

"""
output:
    3.5
    3
"""


print("################### 2 ###################")
print(statistics.harmonic_mean([1,2,3,4,5,6]))
print(statistics.harmonic_mean([2,2,3,3,4,4]))

"""
output:
    2.4489795918367347
    2.769230769230769
"""


print("################### 3 ###################")
print(statistics.median([1,2,3,4,5,6]))
print(statistics.median([2,2,3,3,4,4]))

"""
output:
    3.5
    3
"""


print("################### 4 ###################")
print(statistics.median_low([1,2,3,4,5,6]))
print(statistics.median_low([2,2,3,3,4,4]))

"""
output:
    3
    3
"""


print("################### 5 ###################")
print(statistics.median_high([1,2,3,4,5,6]))
print(statistics.median_high([2,2,3,3,4,4]))

"""
output:
    4
    3
"""


print("################### 6 ###################")
print(statistics.median_grouped([1,2,3,4,5,6]))
print(statistics.median_grouped([1,2,2,3,4,4,4,4,4,5]))

"""
output:
    3.5
    3.7
"""


print("################### 7 ###################")
print(statistics.mode([1,2,2,3]))
print(statistics.mode([1,2,2,3,3,3]))

"""
output:
    2
    3
"""


print("################### 8 ###################")
print(statistics.pstdev([1,2,3,4,5,6]))
print(statistics.pstdev([2,2,3,3,4,4]))

"""
output:
    1.707825127659933
    0.816496580927726
"""


print("################### 9 ###################")
print(statistics.pvariance([1,2,3,4,5,6]))
print(statistics.pvariance([2,2,3,3,4,4]))

"""
output:
    2.9166666666666665
    0.6666666666666666
"""


print("################### 10 ###################")
print(statistics.stdev([1,2,3,4,5,6]))
print(statistics.stdev([2,2,3,3,4,4]))

"""
output:
    1.8708286933869707
    0.8944271909999159
"""


print("################### 11 ###################")
print(statistics.variance([1,2,3,4,5,6]))
print(statistics.variance([2,2,3,3,4,4]))

"""
output:
    3.5
    0.8
"""