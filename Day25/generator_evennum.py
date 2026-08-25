# creating a generator that gives even numbwers 
def numbers():
    for i in range(11):
        yield i
num=numbers()#generator object
for value in num:
    if value %2==0:
        print(value)

