def evens(n):
    for i in range(0, n+1, 2):
        yield i
N = int(input().strip())
first = True
for x in evens(N):
    if not first:
        print (",", end ="")
    print(x, end="")
    first = False
