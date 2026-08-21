#Encapsulation is about protecting data inside class 
#public--anyone can access
class student:
    def std_details(self,name):
        self.name=name#public--anyone can access
student1=student()#obj to class
student1.std_details("deepthi")#calling function
print(student1.name)