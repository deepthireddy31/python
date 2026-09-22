#regex:
#extracting only numbers from a text
import re
marks="marks are 78,92,85"
print(re.findall(r"\d+",marks))