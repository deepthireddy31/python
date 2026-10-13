#coding challenge:
import numpy as np
marks=np.array([78,85,92,67,88,95])
print("Marks:",marks)
print("total-marks:",marks.sum())
print("avg_marks:",marks.mean())
print("highest_marks:",marks.max())
print("lowest_marks:",marks.min())
count=0
for i in marks:
    if i>=85:
        count+=1
print("marks gretaer than 85:",count)
        