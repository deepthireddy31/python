#student details with kwargs (many named values)
def student_profile(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,":",value)
student_profile(Name="charan",Branch="DS",College="CMR",Address="HYD")