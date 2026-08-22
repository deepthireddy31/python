#POTD:online shopping ex
from abc import ABC ,abstractmethod
class product: #parent class
    @abstractmethod
    def __init__(self,product_name,product_price):
        self.product_name=product_name
        self.product_price=product_price
    def show_details(self):#abstract method
            pass
class Laptop(product): #child class
    def show_details(self):
        print("Laptop details:") 
        print("product name:",self.product_name)
        print("price:",self.product_price)
class Mobile(product):
     def show_details(self):
          print("Mobile details:") 
          print("product name:",self.product_name)
          print("price:",self.product_price)
mobile=Mobile("Realme",30000)
laptop=Laptop("HP",25000)
mobile.show_details()
laptop.show_details()
