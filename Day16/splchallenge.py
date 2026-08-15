# sorting list and arranging by highest marks first challenge
students_marks={
    "sudha":69,
    "arya":48,
    "arjun":74,
    "sruthi":81
}
new_marks=list(students_marks.items())
print(type(new_marks))
print(new_marks)
print(sorted(new_marks,key=lambda item: item[1],reverse=True))
