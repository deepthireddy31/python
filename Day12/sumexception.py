#sum exception
try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter another number:"))
    add=num1+num2
    print(f"sum is: {add}")
except ValueError:
    print("invalid input/number")
