#function with std details using both args and normal 
def student_details(name,*args):
    return name,args
print(student_details("sushma",28,42,31,82,40))
