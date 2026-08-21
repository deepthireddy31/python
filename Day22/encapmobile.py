#encapsulation
#with mobile ex and using private
class mobile:
    def password_verified(self,name,price,password):
        self.name=name #public
        self.price=price #public
        self.__password=password #private
        if password=="hello":
            print("password is correct:")
            print(self.name)
mob=mobile()
mob.password_verified("vivo",23000,"hello")
print(mob.price)
#print(mob.__password) cannot access outside class