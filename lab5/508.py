import re

s = input()
pattern = input()

a = re.split(pattern, s)
for i in range(len(a)):
    if i == len(a)-1:
        print(a[i], end="")
    else:
        print(a[i], end=",")