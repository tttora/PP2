import re

s = input()
a = re.compile(r"\d+")
if a.fullmatch(s):
    print("Match")
else:
    print("No match")
