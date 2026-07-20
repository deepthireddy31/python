balance=10000
PIN=int(input("Enter pin:"))
if PIN==1234:
    print("--Menu--")
    print("check Balance")
    print("Deposit")
    print("Withdraw")
    choice=int(input("Enter choice:" ))
    if choice==1:
        print("balance:",balance)
    elif choice==2:
        deposit_amount=int(input("ENter deeposite amount:"))
        new_amount=balance+deposit_amount
        balance=new_amount
        if deposit_amount>0:
            print("current amount:",new_amount)
            print("Total balance:",balance)
        else:
            print("deposit cannot be negative")
    elif choice==3:
        withdrawn_amount=int(input("Enter withdrawn amount:"))
        total_amount=balance-withdrawn_amount
        balance=total_amount#updating balance
        if withdrawn_amount<=balance:
            print("Total amount after withdrawn:",total_amount)
            print("Total balance:",balance)
        else:
            print("Insufficient Balance")
    else:
        print("Invalid choice")
else:
    print("Incorrect pin")

