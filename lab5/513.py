import re
s = input()
a = re.findall(r"\w+", s)
count = len(a)
print(count)
