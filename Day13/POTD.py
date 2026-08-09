#dice game
import random
number=random.randint(1,6)
print(number)
if number==6:
    print("jackpot!")
elif number==1:
    print("Bad luck")
else:
    print("keep playing")
