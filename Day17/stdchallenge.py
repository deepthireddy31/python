#student performance analyzer
def student_marks(*args):
    print(args)
    print(sum(args))
    print(max(args))
    print(min(args))
    pass_count=0
    fail_count=0
    for marks in args:
        if marks>=35:
            pass_count+=1
        else:
            fail_count+=1
    print("passing count:",pass_count)
    print("failing count:",fail_count)        
student_marks(34,78,35,28,31,63,59)
