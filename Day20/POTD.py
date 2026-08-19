#student details with inheritance
class person:                #inherited parent
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
        print("person details")
    def person_details(self):
        print("Name:",self.name)
        print("age:",self.age)
        print("role:",self.role)
class student(person):
    def __init__(self, name, age, role,rollno,marks):
        super().__init__(name, age, role)
        self.rollno=rollno
        self.marks=marks
        print("student details")
    def std_details(self):
        print("role no:",self.rollno)
        print("marks:",self.marks)
std1=student("gorge",23,"manager",34,78)#obj for child class
std1.person_details()
std1.std_details()
s1=student("nancy",43,"HR",67,90)#calling function
s1.person_details()
s1.std_details()
#print("second student:")
#print(s1.name)
#print(s1.age)
#print(s1.role)
#print(s1.rollno)
#print(s1.marks)
