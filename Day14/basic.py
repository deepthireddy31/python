#list comprehension
numbers=[i*i for i in range(1,8)]
print(numbers)
#even numbers displaying with a condition
even_numbers=[i for i in range (1,11) if i%2==0] 
print(even_numbers) 
#using strings
names=["rahul","smith","gorge","priya"]
upper_names=[names.upper() for names in names]
print(upper_names)
