n = int(input())

arr = []
for i in range(n):
    arr.append(input())

unique = []

for s in arr:
    if s not in unique:
        unique.append(s)

unique.sort()

for s in unique:
    print(s, arr.index(s) + 1)
