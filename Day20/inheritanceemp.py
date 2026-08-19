#inheritance with employee
class employee:
    def employee_details(self,name,salary):
        self.name=name
        self.salary=salary
        print("employee class")
class developer(employee):
    def dev_details(self,programming_lan):
        self.programming_lan=programming_lan
developer1=developer()#obj for child class
developer1.employee_details("abdul",9300)
developer1.dev_details("python")
print("employee details")
print(developer1.name)
print(developer1.salary)
print("developer details")
print(developer1.name)
print(developer1.programming_lan)
print(developer1.salary)