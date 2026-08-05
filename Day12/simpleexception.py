#simple exception example;
try:
    num=int(input("Enter a number:"))
    print("Entered:",num)
except ValueError:
    print("Invalid number")