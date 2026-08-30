#reading a file using readline and loops to print eacg line
with open("day26_std.txt","r")as file:
    lines=file.readlines()
for line in lines:
    print(line.strip())
    #strip:remove space in front and back of text