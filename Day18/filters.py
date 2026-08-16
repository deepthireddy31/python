#filters()gives matching data
#keeping only numbers graterthan 50:
numbers=[78,23,67,12,89,45,90]
greaterthan=list(filter(lambda number:number>50,numbers))
print(greaterthan)
#keeping only words length greaterthan 4
words=["AI","Python","data","Ml","science"]
length_words=list(filter(lambda word:len(word)>4,words))
print(length_words)