#grade generator for students marks
marks=[95,82,76,61,43,28,91]
grade=list(map(lambda mark:"A" if mark>=90 else "B" if mark>=80 else"C" if mark>=70 else "D" if mark>=60 else "F" ,marks))
print(grade)