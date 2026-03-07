import re
s = input()

a = re.search(r"Name:\s*([A-Za-z]+),\s*Age:\s*(\d+)" ,s)
print(a.group(1), a.group(2))