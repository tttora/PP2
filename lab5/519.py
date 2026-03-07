import re

s = input()
a = re.compile(r"\w+")
b = re.findall(a,s)
print(len(b))