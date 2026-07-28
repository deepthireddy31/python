#student_record saver coding challege1
file=open("file_challenge.txt","w")
student_name=input("Enter your name:")
Roll_no=input("Enter your Rollno:")
Branch=input("Enter your branch:")
file.write("name: "+ student_name +"\n")
file.write("Rollno: "+ Roll_no +"\n")
file.write("Branch: "+ Branch +"\n")
file.close()
file=open("file_challenge.txt","r")
print(file.read())
#open(..., "w")
#taking input
#close()
#reopening in "r" mode
#print(file.read())