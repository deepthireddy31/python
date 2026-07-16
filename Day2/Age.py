#checking person's age and giving category
Age=int(input("Enter Age:"))
if Age>0 and Age<=12:
    print("child")
elif Age>=13 and Age<=19:
    print("Teenager")
elif Age>=20 and Age<59:
    print("Adult")
else:
    print("Senior Citizen")
