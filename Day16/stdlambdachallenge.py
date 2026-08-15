#student ranking system:
students=[
    ("Deepthi",42),
    ("Rahul",68),
    ("latha",85),
    ("arjun",39),
    ("nova",55),
    ("bolt",22),
    ("suhas",72),
    ("gorge",60),
]
#descending order:
sorted_students=(sorted(students,key=lambda item: item[1],reverse=True))#item[1]=marks,item[0]=names
#sorting std by marks in descending order:
print(sorted_students)
#names in descending order:
for name,marks in sorted_students:
    print(name)
#highest marks obtained std marks,name:
highest_marks=max(sorted_students,key=lambda item:item[1])
print(highest_marks)
#students scored above 70
for name,mark in sorted_students:
    if mark>=70:
        print(name)