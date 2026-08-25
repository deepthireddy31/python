#std marks generator challenge
marks =[34,76,28,12,92,73]
def std_marks():
    for i in marks:
        yield i
mark=std_marks()#generator object
count=0
for mark in marks:
    print("mark:",mark)
    if mark>=35:
        count+=1
print("pssing students count:",count)
