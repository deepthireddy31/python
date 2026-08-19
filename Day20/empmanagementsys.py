#challenge
#Employee management system
class employee:
    def emp_details(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def manager_details(self,department):
        self.department=department
manager1=manager()#obj for child class
manager1.emp_details("smith",78000)
manager1.manager_details("CIVIL")
manager2=manager()
manager2.emp_details("sneha",34000)
manager2.manager_details("Mech")
print("Employee1 details")
print(manager1.name)
print(manager1.salary)
print(manager1.department)
print("Employee2 details")
print(manager2.name)
print(manager2.salary)
print(manager2.department)
