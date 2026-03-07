import re

s = input().split()
count = 0
for i in s:
    if(len(i) == 3):
        count+=1
    
print(count)