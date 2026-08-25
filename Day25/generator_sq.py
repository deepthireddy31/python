#generator that yields square of numbers
def numbers():
    for i in range(1,5):
        yield i*i
num=numbers()
print(next(num))
print(next(num))
print(next(num))
print(next(num))

