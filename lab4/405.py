def cdown(n):
    for i in range(n,-1,-1):
        yield i

n = int(input().strip())
for x in cdown(n):
    print(x)