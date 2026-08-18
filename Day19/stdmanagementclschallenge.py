#student details with oops
class student:
    def __init__(self,name,roll_no,section,branch,marks):
        self.name=name       
        self.roll_no=roll_no        
        self.section=section        
        self.branch=branch        
        self.marks=marks
    #def cal_highest_marks(self):
        #pass
std1=student("bharath","23","C","AIML",67)
std2=student("lasya","62","B","DS",43)
std3=student("anusha","7","A","CSE",52)
highest=max(std1.marks,std2.marks,std3.marks)
print("std1:",std1.name)
print(std1.roll_no)
print(std1.section)
print(std1.branch)
print(std1.marks)
print("std2:",std2.name)
print(std2.roll_no)
print(std2.section)
print(std2.branch)
print(std2.marks)
print("std3:",std3.name)
print(std3.roll_no)
print(std3.section)
print(std3.branch)
print(std3.marks)
print("highest marks:",highest)


