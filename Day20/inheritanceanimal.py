#inheritance for animal ex
class animal():
    def eat(self):
        print("Animal is eating")
        print("Animal ids parent")
class dog(animal):
    def sleep(self):
        print("dog is sleeping")
        print("now,it is barking")
d1=dog()#obj for child class
d1.eat()
d1.sleep()