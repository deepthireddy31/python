#coding challenge 2 student report card
marks=[78,92,75,88,95]
for index, mark in enumerate(marks):
    if mark>=35:
        result="pass"
    else:
        result="fail"
    print(f"student{index}:{mark}:{result}")
