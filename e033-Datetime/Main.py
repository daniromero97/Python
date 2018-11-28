import datetime

print("###################### 1 ######################")
print(datetime.MINYEAR)

"""
output:
    1
"""


print("###################### 2 ######################")
print(datetime.MAXYEAR)

"""
output:
    9999
"""


print("###################### 3 ######################")
print(datetime.date.today())
print("day:", datetime.date.today().day)
print("month:", datetime.date.today().month)
print("year:", datetime.date.today().year)
print("weekday:", datetime.date.today().weekday())

"""
output:
    2018-11-28
    day: 28
    month: 11
    year: 2018
    weekday: 2
"""


print("###################### 4 ######################")
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


print("###################### 5 ######################")
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