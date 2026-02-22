def rev(s):
    for i in range(len(s)-1, -1, -1):
        yield s[i]

s = input().strip()
for x in rev(s):
    print(x, end="")