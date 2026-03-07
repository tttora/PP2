import re

S = input()

a = list(re.findall(r"\d", S))
for i in a:
    print(i, end=" ")