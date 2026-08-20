#coding challenge --payment system
class payment:#parent class
    def pay(self):
        print(payment)
        print("payment is parent class")
        print("payment can be done in 3 ways")
class UPI(payment):
    def pay(self):
        print("UPI:")
        print("UPI is payment method")
        print("UPI is a online mode transaction")
class card(payment):
    def pay(self):
        print("card:")
        print("card is other type of payment mode")
        print("card method should required card to insert/pay")
class cash(payment):
    def pay(self): 
        print("cash:")
        print("cash is another type of payment")
        print("cash is physical way of payment method")
payment1=payment()
cash1=cash()
card1=card()      
upi=UPI()
payment1.pay()
cash1.pay()
card1.pay()
upi.pay()
#instead of calling pay() multiple times use for loop   