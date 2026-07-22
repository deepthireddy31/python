#checking password and is it satisfies all conditions
password=input("Enter your password:")
length=len(password)
has_digit=False
has_upper=False
has_lower=False
for i in password:
    print(i)
    if i.isdigit():
        has_digit=True
    if i.isupper():
        has_upper=True
    if i.islower():
        has_lower=True
if length<8:
    print("length should be atleast 8 characters")
if not has_digit:
        print("password should contain atleast one digit")

if not has_upper:
        print("should contain atleast one uppercase") 
lower=i.islower()
if not has_lower:
        print("should contain atleast one lowercase ")
if length>=8 and has_digit and has_upper and has_lower:
      print("Strong password")
