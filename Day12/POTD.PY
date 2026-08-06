#problem of the day
#function and exception
def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        if b==0:
            return "cannot divide by zero" 
print(safe_divide(10,3))
print(safe_divide(12,0))