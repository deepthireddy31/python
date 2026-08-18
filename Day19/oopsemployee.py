#creating a class employee 
class employee:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
emp1=employee("mohan",30000,"developer")
emp2=employee("priya",45000,"tester")
print(emp1.name)
print(emp1.salary)       
print(emp1.role)
print(emp2.name)
print(emp2.salary)
print(emp2.role)