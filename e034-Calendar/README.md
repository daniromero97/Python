# Calendar

### weekday(year, month, day)

- Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).

```
print(calendar.weekday(2018, 11, 19))
print(calendar.weekday(2018, 11, 21))
print(calendar.weekday(2018, 11, 29))

"""
output:
    0
    2
    3
"""
```


### isleap(year)

- Returns True if year is a leap year, otherwise False.

```
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
```


### leapdays(y1, y2)

- Returns the number of leap years in the range from y1 to y2 (exclusive), where y1 and y2 are years.
- This function works for ranges spanning a century change.

```
print(calendar.leapdays(2020, 2024))
print(calendar.leapdays(2020, 2025))

"""
output:
    1
    2
"""
```


### monthlen(year, month)

- Return the lenght of the month

```
print("monthlen:", calendar.monthlen(2018, 10))
print("monthlen:", calendar.monthlen(2018, 11))
print("monthlen:", calendar.monthlen(2018, 12))

"""
output:
    monthlen: 31
    monthlen: 30
    monthlen: 31
"""
```


### prevmonth(year, month) and nextmonth(year, month)

- Return the previous month and the next month of a month 

```
print("prevmonth:", calendar.prevmonth(2018, 11))
print("nextmonth:", calendar.nextmonth(2018, 11))

"""
output:
    prevmonth: (2018, 10)
    nextmonth: (2018, 12)
"""
```


### monthrange(year, month)

- Returns weekday of first day of the month and number of days in month, for the specified year and month.

```
print("monthrange:", calendar.monthrange(2018, 10))
print("monthrange:", calendar.monthrange(2018, 11))
print("monthrange:", calendar.monthrange(2018, 12))

"""
output:
    monthrange: (0, 31)
    monthrange: (3, 30)
    monthrange: (5, 31)
"""
```


### month(year, month)

- Returns a month’s calendar in a multi-line string using the formatmonth() of the TextCalendar class.

```
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
```

### calendar(year)

- Returns a 3-column calendar for an entire year as a multi-line string using the formatyear() of the TextCalendar class.

```
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
```


### Oficial documentation

- https://docs.python.org/3/library/calendar.html