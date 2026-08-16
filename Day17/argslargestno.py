#finding largest number using args in funtion:
def largest_number(*args):
    print(args)
    print("largest number:",max(args))
largest_number(34,61,84,19,54,29)