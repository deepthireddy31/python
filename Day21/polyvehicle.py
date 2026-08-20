#polymorphism
#vehicle ex without inheritance ,no parent class
class vehicle:
    def move(self):
        print("vehicle moves")
class car():
    def move(self):
        print("car is moving")
class bike():
    def move(self):
        print("bike is moving")
class train():
    def move(self):
        print("train is moving")
train1=train()#object
bike1=bike()
car1=car()
vehicle1=vehicle()
train1.move()#calling method
bike1.move()
car1.move()
vehicle1.move()
#instead of calling move multiple times use for loop but,
#as it is poly without inheritance create init for every class