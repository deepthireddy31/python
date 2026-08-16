#function with employee_details using kwargs(accepts many named values)
def employee_details(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,":",value)
employee_details(emp_name="preethi",age=36,role="developer",experience=3)
#student details
def student_details(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
student_details(Name="mohan",Branch="cyber security",college="JNTU")