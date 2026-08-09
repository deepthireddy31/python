#random password starter
import random
chars=["A","B","C","1","2","3","@","#"]
password=""
for ch in range(4):
    select=random.choice(chars)
    password=password+select
print(password)
    