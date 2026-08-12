#revision of all toipcs which i have learned so far
#student details using dictionaries:
students=[
    {"name":"deepthi","marks":"56"},
    {"name":"john","marks":"86"},
    {"name":"petter","marks":"46"}
]
print(students)
for student in students:
    print("names:",student["name"])
for student in students:
    print("marks:",student["marks"])
#students scored above 80 
marks={
    "rahul":78,
    "amith":45,
    "krupa":92,
    "akshitha":83
}
marks_above=[mark for name,mark in marks.items() if mark>=80 ]
print("marks above 80:",marks_above)
#highest marks among all students
#creating empty list appending marks and using max 
score=[]
score.append(34)
score.append(73)
score.append(92)
score.append(32)
score.append(89)
score.append(63)
score.append(50)
print(score)
highest_marks=max(score)
print(highest_marks)
