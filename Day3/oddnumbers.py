#printing odd numbers using for loop
for i in range(1,21,2):
    print(i)
#using continue for above
# continue:skips current iteration
print("using continue")
for i in range(1,21,2):
    if i==19:
        continue
    print(i)
 