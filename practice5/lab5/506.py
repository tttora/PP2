import re

s = input()

pattern = r"\S+@\S+\.\S+"
a = re.search(pattern, s)
print(a.group() if a else "No email")