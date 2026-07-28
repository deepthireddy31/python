#file name is filesmycollegewith.txt.py (as using withopen)
with open("filescollege.txt","r")as file:
    print(file.read())
    file.close()