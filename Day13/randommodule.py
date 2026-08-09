#random module 
import random
num=random.randint(1,10)
print(num)
guess=int(input("Enter any number:"))
if guess==num:
    print("correct number was:",num)
else:
    print("wrong guess")