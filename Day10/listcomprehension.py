#list comprehension practise Questions
#creating  list using list comprehension
#list comprehensio[expression for variable in sequence]
print("--numbers from 1 to 10 using list comprehension--")
numbers=[i for i in range(1,11)]
print("numbers",numbers)
print("--squares from 1 to 5--")
squares=[i*i for i in range(1,6)]
print("--square number--:",squares)
print("--creating a list containing odd numbers-- ")
odd_numbers=[i for i in range(1,16) if i%2==1]
print("--odd numbers--:",odd_numbers)
#string to uppercase
fruits=["apple","mango","orange"]
fruits_upper=[item.upper()  for item in fruits]
print(fruits_upper)
print("--numbers greater than 18--")
numbers=[10,15,20,25,30]
new_numbers=[items for items in numbers if items>=18 ]
print(new_numbers)