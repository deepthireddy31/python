#exception using list index
#for invalid index 
try:
    names=["deepthi","rahul","sudha","preethi"]
    print(names[3])
except IndexError:
    print("Index out of range")