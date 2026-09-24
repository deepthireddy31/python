#smart file checker
import os
filename=input("Enter filename:")
if (os.path.exists(filename)):
    print("file found",filename)
else:
    print("file not found")
#only checkes files in python project
