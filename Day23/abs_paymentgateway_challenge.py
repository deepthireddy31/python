#coding challenge payment gateway
from abc import ABC ,abstractmethod
class payment_gateway:#parent class
    @abstractmethod
    def __init__(self,amount):#used by all child classes
            self.amount=amount
    def pay(self):
        pass #abstract method
    def payment(self):
        print("payment gateway --- concrete method")#concerete method
class UPI(payment_gateway):#child class
    def pay(self):
        print("UPI payment is sucessfull")
class Credit_Card(payment_gateway):
    def pay(self):
        print("Creadit Card payment successfull")
class Debit_card(payment_gateway):
    def pay(self):
        print("Debit Card is payment is successfull")
upi=UPI(3480)
credit=Credit_Card(2700)
debit=Debit_card(400)
upi.payment()
for i in (upi,credit,debit):
    print("amount:",i.amount)
    i.pay()
