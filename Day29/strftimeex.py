#strfdate:converting from date to string format
from datetime import datetime
date=datetime(2026,8,29)
print(date.strftime("%d-%B-%Y"))
print(date.strftime("%d-%B-%Y-%A"))
#datetime format--year,month,date