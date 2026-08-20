#polymorphism with inheritance
#exployee ex 
class employee:#parent class
    def __init__(self,name):#used by all child classes
        self.name=name
    def work(self):
        print("employee is parent class")
class  developer(employee):#child class
    def work(self):#override
         print("develpoer:developing a website")
         print("developer will develope a project")
class manager(employee):#child class
    def work(self):
         print("manager manages everyone work")
         print("manager has superier to workers below them")
employee1=employee("krishna")#objects
manager1=manager("deepthi")
developer1=developer("dhanush")
#employee1.work()
#manager1.work()
#developer1.work()
#instead of above use this
for x in (employee1,manager1,developer1):
    print(x.name)
    x.work()