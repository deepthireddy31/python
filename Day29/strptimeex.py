#strptime:converts string to date
from datetime import datetime
date=datetime.strptime("15-01-2024","%d-%m-%Y")
print(date)
#datetime format--year,month,date