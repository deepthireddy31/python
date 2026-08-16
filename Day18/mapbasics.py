#map()changes every item in a list
numbers=[5,10,15,20,25]
twice_numbers=list(map(lambda x:x*2,numbers))
print(twice_numbers)
#converting names into uppercases
names=["deepthi","anad","pooja","somu"]
upper_case=list(map(lambda name:name.upper(),names))
print(upper_case)