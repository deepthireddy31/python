#challenge:safe student calculator
try:
    sub1_marks=int(input("Enter sub1 marks:"))
    sub2_marks=int(input("Enter sub2 marks:"))
    sub3_marks=int(input("Enter sub3 marks:"))
    total=(sub1_marks+sub2_marks+sub3_marks)
    average=total/3
    if average>=90:
           grade="A"
    elif average>=80:
            grade="B"
    elif average>=70:
            grade="C"
    elif average>=60:
            grade="D"
    else:
            grade="F"
except ValueError:
       print("Pleaes enter valid numberic marks")
else:
       print("Total:",total)
       print("Average:",average)
       print("Grade:",grade)