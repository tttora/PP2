import re

s = input()
count = 0
for i in range(len(s)):
    a = re.match(r"[A-Z]", s[i])
    if a:
        count += 1
print(count)
