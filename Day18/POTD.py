#Create a function analyze_numbers(numbers) that:
def analyze_numbers(*numbers):
    print(numbers)
    #removes all odd numbers using filter(),
    even_numbers=list(filter(lambda num:num%2==0,numbers))
    print(even_numbers)
    #squares the remaining numbers using map()
    squaring_numbers=list(map(lambda num:num*num,even_numbers))
    print(squaring_numbers)
#returns the final list.
analyze_numbers(2,3,4,5,6,7,12,58,11,15)
