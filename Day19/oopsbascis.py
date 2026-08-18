#creating class and object to that class
class student:
    pass
std1=student()
print(std1)
#class with variables and init function
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("deepthi",23)
s2=student("bean",43)
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)
    
