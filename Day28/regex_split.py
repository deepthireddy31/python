#regex:
#using split:splits using a pattern
import re
colors="red,blue;green yellow-pink"
print(re.split("[,; -]",colors)) #splits each word with comma