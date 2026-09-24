#coding challenge:student attendence data system
from datetime import datetime
name=input("Enter your name:")
print("Student:",name)
now=datetime.now()
print("Date:",now.date())
print("Day:",now.strftime("%A"))
print("Time:",now.time())