#polymorphism
#vehicle ex with inheritance
class shape:
    def area(self):
        print("shape having circle,rectangle")
class circle(shape):
    def area(self,radius):#override
        self.radius=radius
        print("circle")
        print("area of circle:",2*radius*radius)#calculating area of circle
class rectangle(shape):
    def area(self,breadth,length):
        self.breadth=breadth
        self.length=length
        print("rectangle")
        print("area of rectangle:",length*breadth)
shape1=shape()#object
rect1=rectangle()
circle1=circle()
shape1.area()#calling function
circle1.area(34)#passing arugments
rect1.area(3,6)