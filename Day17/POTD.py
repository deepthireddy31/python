#function with args
def student(*args):
    print(args)
    print("total:",sum(args))
    print("average:",sum(args)/len(args))
    print("maximum:",max(args))
    print("minimum:",min(args))
student(34,72,69,17,51,84)