#student data analyzer
students={
    "deepthi":99,
    "nova":45,
    "arjun":73,
    "rahul":95
}
print(students) 
names=[name for name, mark in students.items()]
print(names)
marks=[mark for name, mark in students.items()]
print(marks)
#students scored above 80 
marks_above=[mark for name,mark in students.items() if mark>=80 ]
print(marks_above)
highest_marks=max(students.values())
print(highest_marks)
#to get topper name
for name,mark in students.items():
    if mark==highest_marks:
        print(name)