#tuple with loop
colours=("red","blue","orange","green","yellow")
for item in colours:
    print("colours:",colours)
#changing  value in the tuple
colours=("red","blue","orange","green","yellow")
colours[1]="pink"#repalcing
print(colours)#gives error as tuple not allow changes