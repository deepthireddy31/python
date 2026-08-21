#encapsulation
#private:"__" used and can only acces within class ,with function in the class
class bankaccount:
    def __init__(self,bank_name,balance):
        self._bank_name=bank_name  #protected
        self.__balance=balance   #private
    def bank_details(self):
        print(self.__balance)
        print(self._bank_name)
bank=bankaccount("SBI",45000)
bank.bank_details()
print("protected outside the class:")
print(bank._bank_name) 
    