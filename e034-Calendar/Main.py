import calendar

print("##################### 1 #####################")
print(calendar.weekday(2018, 11, 19))
print(calendar.weekday(2018, 11, 21))
print(calendar.weekday(2018, 11, 29))

"""
output:
    0
    2
    3
"""


print("##################### 2 #####################")
print(calendar.isleap(2018))
print(calendar.isleap(2020))
print(calendar.isleap(2024))
print(calendar.isleap(2025))

"""
output:
    False
    True
    True
    False
"""


print("##################### 3 #####################")
print(calendar.leapdays(2020, 2024))
print(calendar.leapdays(2020, 2025))

"""
output:
    1
    2
"""


print("##################### 4 #####################")
print("monthlen:", calendar.monthlen(2018, 10))
print("monthlen:", calendar.monthlen(2018, 11))
print("monthlen:", calendar.monthlen(2018, 12))

"""
output:
    monthlen: 31
    monthlen: 30
    monthlen: 31
"""


print("##################### 5 #####################")
print("prevmonth:", calendar.prevmonth(2018, 11))
print("nextmonth:", calendar.nextmonth(2018, 11))

"""
output:
    prevmonth: (2018, 10)
    nextmonth: (2018, 12)
"""


print("##################### 6 #####################")
print("monthrange:", calendar.monthrange(2018, 10))
print("monthrange:", calendar.monthrange(2018, 11))
print("monthrange:", calendar.monthrange(2018, 12))

"""
output:
    monthrange: (0, 31)
    monthrange: (3, 30)
    monthrange: (5, 31)
"""


print("##################### 7 #####################")
print(calendar.month(2018, 11))     # monthrange = 3
print(calendar.month(2018, 12))     # monthrange = 5

"""
output:
       November 2018
    Mo Tu We Th Fr Sa Su
              1  2  3  4
     5  6  7  8  9 10 11
    12 13 14 15 16 17 18
    19 20 21 22 23 24 25
    26 27 28 29 30
    
       December 2018
    Mo Tu We Th Fr Sa Su
                    1  2
     3  4  5  6  7  8  9
    10 11 12 13 14 15 16
    17 18 19 20 21 22 23
    24 25 26 27 28 29 30
    31
"""


print("##################### 8 #####################")
print(calendar.calendar(2018))

"""
output:
                                      2018
    
          January                   February                   March
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7                1  2  3  4                1  2  3  4
     8  9 10 11 12 13 14       5  6  7  8  9 10 11       5  6  7  8  9 10 11
    15 16 17 18 19 20 21      12 13 14 15 16 17 18      12 13 14 15 16 17 18
    22 23 24 25 26 27 28      19 20 21 22 23 24 25      19 20 21 22 23 24 25
    29 30 31                  26 27 28                  26 27 28 29 30 31
    
           April                      May                       June
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                       1          1  2  3  4  5  6                   1  2  3
     2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10
     9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17
    16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24
    23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30
    30
    
            July                     August                  September
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                       1             1  2  3  4  5                      1  2
     2  3  4  5  6  7  8       6  7  8  9 10 11 12       3  4  5  6  7  8  9
     9 10 11 12 13 14 15      13 14 15 16 17 18 19      10 11 12 13 14 15 16
    16 17 18 19 20 21 22      20 21 22 23 24 25 26      17 18 19 20 21 22 23
    23 24 25 26 27 28 29      27 28 29 30 31            24 25 26 27 28 29 30
    30 31
    
          October                   November                  December
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7                1  2  3  4                      1  2
     8  9 10 11 12 13 14       5  6  7  8  9 10 11       3  4  5  6  7  8  9
    15 16 17 18 19 20 21      12 13 14 15 16 17 18      10 11 12 13 14 15 16
    22 23 24 25 26 27 28      19 20 21 22 23 24 25      17 18 19 20 21 22 23
    29 30 31                  26 27 28 29 30            24 25 26 27 28 29 30
                                                        31
"""
