#abstraction:which means showing only the essential functionality and hiding the implementation details
#abc module provides tools for creating Abstract Base classes
from abc import ABC,abstractmethod #abc module
class animal(ABC): #abstract class
    @abstractmethod
    def sound(self): #abstarct method:has no data in it
        pass #no implementation here
class dog(animal): #child class -- which implementsS
    def sound(self):  #which allows subclaees define their own behaviour 
        print("dog barks")
        print("abstartion")
dog1=dog()
dog1.sound()
