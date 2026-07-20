#Number guessing game where user have limited chances to guess correct number. 
for i in range(3): 
   number=int(input("Enter number:"))
   correct_number=34
   if number==correct_number:
    print("congratulations! you guessed correctly.")
    break 
   else:
    print("Try again.")
else:
    print("Game over")