def power(n):
    for i in range(0,n+1):
        yield 2 ** i

n = int(input().strip())
for x in power(n):
    print(x, end=" ")