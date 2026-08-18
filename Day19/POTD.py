#about bank
class BankAccount:
    def __init__(self,account_holder,balance,deposite):
        self.account_holder=account_holder
        self.balance=balance
        self.deposite=deposite
    def cal_account_details(self):
        return self.balance+self.deposite
deposit1=BankAccount("mohan",6700,3090)
deposit2=BankAccount("balu",10300,3400)
print("account holder:",deposit1.account_holder)
print("balance amount:",deposit1.balance)
print("deposit amount:",deposit1.deposite)
print("final amount:",deposit1.cal_account_details())
print("account holder:",deposit2.account_holder)
print("balance amount:",deposit2.balance)
print("deposit amount:",deposit2.deposite)
print("final amount:",deposit2.cal_account_details())

