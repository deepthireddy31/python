#division exception
try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter another number:"))
    divide=num1/num2
    print("division:",divide)
except ZeroDivisionError:
    if num2==0:{
            print("cannot divide with zero")
    }