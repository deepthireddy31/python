#calculating area of rectangle with oops
class rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def calculate_area(self):#another function
            return self.length*self.width
len1=rectangle(45,20)
len2=rectangle(20,89)
print(len1.length)
print(len2.width)
print("Area of rectangle is:",len1.calculate_area())
print("Area if rectangle is:",len2.calculate_area())
#to cal area create obj and call (cal_area function) to get area