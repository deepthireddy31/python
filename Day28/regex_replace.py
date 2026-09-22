#regex:
#using resub():replace text
import re
text="java is fun"
new_text=re.sub("java","python",text)
print(new_text)