#Encapsulation:three attribute
class person:
    def __init__(self,name,age,address,job):
        self.name=name#public
        self._age=age #protected
        self.__address=address #private
        self.__job=job #private
    def person_details(self):
        print(self.__address)
        print(self.__job)
        print(self._age)
        print(self.name)
person1=person("madhu",32,"mumbai","fasion designer")
person1.person_details()
print("--public-- anyone can access")
print(person1.name)
print(person1._age)
#print(person1.__address) cannot access outside class