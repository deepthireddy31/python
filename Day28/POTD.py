#login validation:
import re
email="deepthi123@gmail.com"
password="python@123"
print(re.search(r"\w+@\d+",password))
#r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*!]).{8,}$"
# flow for above patern :
# start → has lowercase → has uppercase → has digit → has special character → at least 8 characters → End.