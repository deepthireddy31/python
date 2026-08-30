#adding new data in already exisiting file(day26_std.txt)
#if file not found it creates a file and add information
with open("day26_std.txt","a") as file:
    file.write("\npython learner")
    file.write("\n appending text")