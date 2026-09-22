#regular expressions (re):It is used for search,match,extract,replace ans validate text
#using re.search:searching for a word in a text
import re
text="I love python programming"
result=re.search("python",text)
print(result) #gives the match or not
print(result.group()) #gives the word we are matching if present
