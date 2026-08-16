#Normal function
def numbers(a,b):
    return a+b
print(numbers(23,45))#if we give more 2 values it gives error.so, args are used for many values in function
#using args 
#args:accepts many values and stores in tuple
def show_numbers(*args):
    print(type(args))#tuple
    print(args)
    print("sum:",sum(args))
show_numbers(78,56,23,1,85,2)
#practice 
#calculate sum for any no of numbers
def calculate_sum(*args):
    print(args)
    print("calculated sum:",sum(args))
calculate_sum(34,10,50,20,40,61.45)
