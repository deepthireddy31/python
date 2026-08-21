#encapsulation
#protected:"_" used and can acces within class ,but it is convention
class employee:
    def __init__(self,name,salary):
        self.name=name       #public
        self._salary=salary    #protected
employee1=employee("raghu",7800)
print(employee1.name)
print(employee1._salary) 