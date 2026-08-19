#inheritance with persons ex
class parent:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def parent_details(self):
        print("this is parent class")
p1=parent("raju",34,"hyd")
s1=parent("rahul",54,"mlg")
class student(parent):
    def student_details(self,branch):
        self.branch=branch
        print("branch is data science")
std_details=student("laya",45,"hyd")#obj for child class
std_details.parent_details()
std_details.student_details("AIML")
print("parent details")
print(p1.name)
print(p1.age)
print(p1.address)
print(s1.name)
print("student details:")
print(std_details.name)
print(std_details.age)
print(std_details.address)
print(std_details.branch)

