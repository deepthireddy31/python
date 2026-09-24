#priting individual date time etc
from datetime import datetime
now=datetime.now()
print(now)
print("date:",now.date())
print("year:",now.year)
print("month:",now.month)
print("day:",now.day)
print("time:",now.time())
print("hour:",now.hour)
print("minute",now.minute)
print("seconds:",now.second)