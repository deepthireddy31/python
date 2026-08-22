#abstraction with vehicle,concrete method ex
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def move(self):#abstarct method:not implemented it shoud be override in subclass to implement
        pass
    def vehicle_move(self): #concrete method :which is fully implemented in abs class
        print("---This concrete class----")
        print("vehicle moving") 
class car(vehicle):
    def move(self):
        print("car is child class of vehicle")
        print("car is moving")
class bike(vehicle):
    def move(self):
        print("bike is another child class of vehicle")
        print("bike is moving")
bike1=bike()
car1=car()
bike1.move()
car1.move()
bike1.vehicle_move() #with any child object we can call it
#as vehicle_move is already implemented(concrete class) the child class can use directly