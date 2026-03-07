import re
s = input()
p = input()
a = re.findall(re.escape(p), s)
print(len(a))