#student attendence manager challenge:
with open("day27_attendence.txt","w")as file:
    file.write("deepthi")
    file.write("\ndhanush") 
    file.write("\nlatha")
with open("day27_attendence.txt","a")as file:
    file.write("\njohn")
with open("day27_attendence.txt","r")as file:
    lines=file.readlines()
    count=(len(lines))
    print("total students:",count)