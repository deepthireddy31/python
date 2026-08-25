#POTD:creating generator and loop
def counter():
    for i in range(1,11):
        yield i
count=counter()#generator obj
for value in counter():
    print(value)

