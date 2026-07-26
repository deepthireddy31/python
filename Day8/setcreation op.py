#creating set and performing operations
names={"deepthi","arjun","nova","bolt","aravind"}
print(names)
print(type(names))
#adding elements into exsisting set
names.add("nancy")
print(names)
#removing elements
names.remove("bolt")
names.remove("deepthi")
print(names)
#membership operation(checks if an element exists)
print("deepthi" in names)
print("arjun" in names)
#removing duplications in list using sets
numbers=[29,60,45,76,29,34,60]
new_numbers=set(numbers)
print(new_numbers)
print(type(new_numbers))
