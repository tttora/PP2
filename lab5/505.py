import re

s = input()
pattern = r"^[A-Za-z].*[0-9]$"
print("Yes" if re.search(pattern, s) else "No")