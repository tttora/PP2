import re

s = input()

a = re.search(r"cat|dog", s)
print("Yes" if a else "No")