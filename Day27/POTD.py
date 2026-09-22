#secret txt file
with open("day27_secret.txt","r")as file:
    print(file.read())
    file.seek(0)   #go back to the baginning
    print(file.readlines())