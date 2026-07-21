#student result system challenge
maths=int(input("Enter maths marks:"))
physics=int(input("Enter physics marks:"))
chemistry=int(input("Enter chemistry marks:"))
total=maths+physics+chemistry
average_marks=total/3
def calculate_total(marks):
    print("Total marks are:",marks)
calculate_total(total)
def calculate_average(average_marks):
    print("the average marks are:",average_marks)
def calculate_grades(average_marks):
    print("grades",average_marks )
calculate_average(average_marks)
if average_marks>=90:
    calculate_grades("A")
elif average_marks>=80:
    calculate_grades("B")
elif average_marks>=70:
    calculate_grades("C")
elif average_marks>=60:
    calculate_grades("D")
else:
    calculate_grades("F")



            
            
        
            
