def tosquare(n):
    for i in range (1, n+1):
        yield i ** 2

N = int(input().strip())
for a in tosquare(N):
    print(a)