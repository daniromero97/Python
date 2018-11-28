# datetime

- The datetime module supplies classes for manipulating dates and times in both simple and complex ways.
- While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.


### Constants

##### MINYEAR

- The smallest year number allowed in a date or datetime object. MINYEAR is 1.

```
print(datetime.MINYEAR)

"""
output:
    1
"""
```

##### MAXYEAR

- The largest year number allowed in a date or datetime object. MAXYEAR is 9999.

```
print(datetime.MAXYEAR)

"""
output:
    9999
"""
```

##### date

```
print(datetime.date.today())
print("day:", datetime.date.today().day)
print("month:", datetime.date.today().month)
print("year:", datetime.date.today().year)
print("weekday:", datetime.date.today().weekday())

"""
output:
    99992018-11-28
    day: 28
    month: 11
    year: 2018
    weekday: 2
"""
```

##### datetime

```
print(datetime.datetime.now())
print("hour:", datetime.datetime.now().hour)
print("minute:", datetime.datetime.now().minute)
print("second:", datetime.datetime.now().second)
print("microsecond:", datetime.datetime.now().microsecond)
print("timestamp():", datetime.datetime.now().timestamp())

"""
output:
    2018-11-28 12:54:24.378262
    hour: 12
    minute: 54
    second: 24
    microsecond: 378290
    timestamp(): 1543406064.378299
"""
```


##### timedelta

```
print("weeks:", datetime.timedelta(weeks=1), "--> total seconds:",datetime.timedelta(weeks=1).total_seconds())
print("days:", datetime.timedelta(days=1), "--> total seconds:",datetime.timedelta(days=1).total_seconds())
print("hours:", datetime.timedelta(hours=1), "--> total seconds:",datetime.timedelta(hours=1).total_seconds())
print("minutes:", datetime.timedelta(minutes=1), "--> total seconds:",datetime.timedelta(minutes=1).total_seconds())
print("seconds:", datetime.timedelta(seconds=1), "--> total seconds:",datetime.timedelta(seconds=1).total_seconds())
print("milliseconds:", datetime.timedelta(milliseconds=1), "--> total seconds:",datetime.timedelta(milliseconds=1).total_seconds())
print("microseconds:", datetime.timedelta(microseconds=1), "--> total seconds:",datetime.timedelta(microseconds=1).total_seconds())
print("total:",
      datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1, milliseconds=1, microseconds=1),
      "--> total seconds:",
      datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1, milliseconds=1, microseconds=1).total_seconds())

"""
output:
    weeks: 7 days, 0:00:00 --> total seconds: 604800.0
    days: 1 day, 0:00:00 --> total seconds: 86400.0
    hours: 1:00:00 --> total seconds: 3600.0
    minutes: 0:01:00 --> total seconds: 60.0
    seconds: 0:00:01 --> total seconds: 1.0
    milliseconds: 0:00:00.001000 --> total seconds: 0.001
    microseconds: 0:00:00.000001 --> total seconds: 1e-06
    total: 8 days, 1:01:01.001001 --> total seconds: 694861.001001
"""
```


##### date formatting

```
print(datetime.date.today())
print(datetime.datetime.today().strftime('%d, %b %Y'))
print(datetime.datetime.now())
print(datetime.datetime.now().strftime('%d, %b %Y'))
print(datetime.datetime.now().strftime('%d/%b/%Y %H:%M:%S'))


"""
output:
    2018-11-28
    28, Nov 2018
    2018-11-28 13:26:41.492853
    28, Nov 2018
    28/Nov/2018 13:26:41
"""
```


##### Oficial documentation

- https://docs.python.org/3/library/datetime.html
