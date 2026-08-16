#Normal function:
def student(name,age):
    return name,age
print(student("deepthi",23))#accepts only 2(defined values)
#using kwargs:
#kwargs accepts many named(key value pair values)and stores in dictionary
def student_details(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key,value in  kwargs.items():
        print(key,":",value)
student_details(name="suhas",age=26,branch="AIML")

