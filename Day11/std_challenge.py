#student result analyser
marks=[34,56,98,66,84,49]
def analyze_student(mark):
    total=sum(mark)
    average=total/len(mark)
    highest_marks=max(mark)
    lowest_marks=min(mark)
    if average>=90:
       grade="A"
    elif average>=80:
        grade="B"
    elif average>=70:
        grade="C"
    elif average>=60:
        grade="D"
    else:
        grade="F"
    return total,average,highest_marks,lowest_marks,grade
total,average,highest,lowest,grade=analyze_student(marks)
print("marks:",marks)
print("total:",total)
print("average:",average)
print("highest marks:",highest)
print("lowest marks:",lowest)
print("grade:",grade)




