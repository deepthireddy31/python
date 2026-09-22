#"with" releated basics examples
#writing file
with open("day27_with.txt","w")as file:
    file.write("\npython")
    file.write("\nSQL")
    file.write("\nJava")
#appending new text
with open("day27_with.txt","a")as file:
    file.write("\ndata science")
#reading file
with open("day27_with.txt","r")as file:
    print(file.read())
#after with statement check whether file closed or not
print(file.closed)#True
