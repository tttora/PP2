import re

s = input()
a = re.sub(r"(\d)", r"\1\1", s)
print(a)