#list and function 
#print highest number
def number(number):
    number=[10,45,78,23]
    largest_num=max(number)
    return largest_num
    #return number(to print all numbers)
print(number(number))
#list and average marks
def marks(marks):
    marks=[80,90,70]
    average_marks=sum(marks)/3
    return average_marks#stores and returns 
print(marks(marks))
#max,mun
def numbers(numbers):
    numbers=[23,54,63,88,43,21]
    maximun=max(numbers)
    minimun=min(numbers)
    return maximun,minimun
print(numbers(numbers))
#list function and uppercase
names=["papaya","mango","apple","banana","pineapple"]
new_names=[]
for item in names:
    capital=item.upper()
    new_names.append(capital)
print(new_names)
    
