#polymorphism:same method with different behaviour
class Animal:#parent class
    def sound(self):
        print("Animal")#not appears
class dog(Animal):
    def sound(self):#oveeride
        print("dog barks")
        print("dog is child")
class cat(Animal):
    def sound(self):
        print("cat meow")
        print("cat is child")
Animal1=Animal() 
dog1=dog()#object of dog class
cat1=cat()#object of cat class
dog1.sound()#calling with method
cat1.sound()
Animal1.sound()
#polymorphism with inheritance --- overrides a method
#polymorphism without inhertitance---uses same method not override
