import re

s = input()
a = re.findall(r"\d{2}/\d{2}/\d{4}", s)
print(len(a))