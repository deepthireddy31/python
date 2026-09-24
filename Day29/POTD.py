#POTD:birthday countdown
from datetime import datetime
currentdate=datetime.now()
birthdaydate=datetime(2027,3,13)
print(currentdate)
if currentdate.month == birthdaydate.month and currentdate.day == birthdaydate.day:
#if currentdate.date()==birthdaydate.date():
    print("Happy Birthday!")
else:
    print("Remaining:",birthdaydate.date()-currentdate.date())