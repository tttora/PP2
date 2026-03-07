#Read two lines: a string  and a pattern  (literal string, no special regex symbols). Using re.findall() or re.finditer(), count how many times  appears in  as a non-overlapping match. Output the count

import re

S = input()
P = input()

count = len(list(re.finditer(P, S)))
print(count)