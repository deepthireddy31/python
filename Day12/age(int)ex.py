#user age taking as input and exception handling if invalid input provided: 
try:
    Age=int(input("Enter your age:"))
    print("age:",Age)
except ValueError:
    print("Age must be a number")
