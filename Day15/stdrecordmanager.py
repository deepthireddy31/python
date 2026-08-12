#Create a program that:
#stores at least 4 students in a list of dictionaries,
student_details={
    "raghu":43,
    "madhu":78,
    "teja":34,
    "nandhu":88
}
#printing all student details,
print(student_details)
print(type(student_details))
#prints students who passed (marks >= 35),
std_passed=[name for name,marks in student_details.items() if marks>=35]
print("passed std:",std_passed)
#prints students who scored distinction (marks >= 75),
std_dist=[name for name,marks in student_details.items() if marks>=75]
print("Distinction std:",std_dist)
#calculates the class average,
#for name,marks in student_details.items():
total_marks=[mark for name,mark in student_details.items()]
total=sum(total_marks)
average=total/4
print("total:",total)
print("class average:",average)
#prints the topper name and mark.
#std_dist=[name for name,marks in student_details.items()]
highest_marks = max(student_details.values())

for name, mark in student_details.items():
    if mark == highest_marks:
        print("Topper:", name, "-", mark)