import re

f = open("blex_test.xml", "r")
#f = open("BLex_03.xml", "r")

matches = re.findall(r"<italic>[\w\s]*<\/italic>", f.read())

print(matches) 
