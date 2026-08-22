#abstarction with shape ex and init function
from abc import ABC ,abstractmethod
class shape():
    @abstractmethod
    def __init__(self):
        pass
    def area(self):
        pass
    def draw(self):
        print("concrete class")
        print("drawing the shapes")
class circle(shape):
    def area(self,radius):
        self.radius=radius
        return 3.14*radius*radius
class rectangle(shape):
    def area(self,length,breadth):
        self.length=length
        self.breadth=breadth
        return length*breadth
rect=rectangle()
circle1=circle()
print(rect.area(34,56))# as return is used print is written
print(circle1.area(2))