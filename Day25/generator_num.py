#generator--uses yields
#yield--pauses the function
#next--continues
def numbers():
  yield 1
  yield 2
  yield 3
  yield 4 
  yield 5
num=numbers()
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
#another way
def numbers():
    for i in range(1,6):
        yield i
num=numbers()#create the generator object
print("other method")
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
