#lambda function
#creating a lambda function and doubling a  number 
number=lambda x:x*2
print(number(34))
print(number(41))
print(number(98))
print(number(62))
#printing large number:
numbers=[23,8,56,230,11,183]
large_number=lambda number: max(number)
print("large number:",large_number(numbers))
#sorting ascending order:
marks=[78,45,81,36,88,20]
print("ascending order:",sorted(marks))
#descending order:
print("descendong order:",sorted(marks, reverse=True))
#sorting a list according with their length
names=["Deepthi","Ai","Data","Rahul","bag","gouri"]
length=sorted(names,key=lambda name:len(name))
print(length)