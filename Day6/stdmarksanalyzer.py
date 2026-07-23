marks=[80,76,89,92,98]
total_marks=sum(marks)
average_marks=total_marks/5
print("total marks are:",total_marks)
print("average marks:",average_marks)
print("highest marks:",max(marks))
print("lowest marks:",min(marks))
count=0
for i in marks:
      if i >=90:
        count=count+1
print("scored above 90:",count)
#list_name.count(element)