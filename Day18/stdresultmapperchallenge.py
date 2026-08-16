#student result mapper challenge:
names=["deepthi","rahul","suhas","satya"]
marks=[34,78,52,37]
#combine both lists using zip():
combined=list(zip(names,marks))
print("combined both names & marks:",combined)
#printing each std names & marks:
print( "names & marks of the students:",combined)
#using filters to get marks above 35
passing_marks=list(filter(lambda marks:marks>=35,marks))
print(passing_marks)
#using maps to add 5 bonus marks to every mark 
bonus_marks=list(map(lambda mark:mark+5,marks))
print("after adding bonus marks:",bonus_marks)