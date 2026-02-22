def div(n):
    for i in range(n+1):
        yield i

N = int(input().strip())
for x in div(N):
    if x % 3 == 0 and x % 4 == 0:
        print(x, end = " ")