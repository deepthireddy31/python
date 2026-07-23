#creating list and using list methods
numbers=[10,20,70,30,40]
#insert & append()using add method and append method
numbers.insert(4,50)
print("insert",numbers)
numbers.append(60)
print("append",numbers)
#when we insert a value then next we have the updated list 
#remove method:when know which value to delete
print("remove method")
numbers.remove(20)
print("list after 20 is removed",numbers)
numbers.pop()#delete the last element 
print("list with pop",numbers)
numbers.pop(3)#deletes value with specified index
print("pop with index",numbers)
#updating list values:changes the old value with new value
print("updating method")
numbers[2]=100#40-100
print(numbers)
#slicing
print("list with slicing")
print(numbers[1:])
print(numbers[-2:-1])#ending index not included
#sorting in list
print("sorting in list ")
numbers.sort()#ascending order
print("sorting ascending order:",numbers)
numbers.reverse()#prints list reverse order
print("reverse method:",numbers)
numbers.sort(reverse=True)#descending order
print("sorting descending order:",numbers)


