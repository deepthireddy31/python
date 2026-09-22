#student information extractor:
import re 
text="""deepthi - marks: 92
rahul - marks: 78
nova - marks: 85"""
print(re.findall(r"^[A-Za-z]+",text,re.MULTILINE))
print(re.findall(r"\d+",text))