import re

S = input()
P = input()

print("Yes" if re.search(P, S) else "No")