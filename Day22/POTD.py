#POTD:ATM system
class atm:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder #public
        self.__balance=balance #private
    def check_balance(self):
        print(self.account_holder)
        print(self.__balance)
    def deposit(self,deposit_amount):
        self.deposit_amount=deposit_amount
        print("initial balance:",self.__balance)
        print("deposit:",self.deposit_amount)
        print("updated balance:",self.__balance+self.deposit_amount)
ATM=atm("bunty",8900)
ATM.check_balance()
ATM.deposit(3400)
