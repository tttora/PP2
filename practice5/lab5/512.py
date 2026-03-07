import re
s = input()

a = re.findall(r"\d{2,}", s)
for i in a:
    print(i, end=" ")