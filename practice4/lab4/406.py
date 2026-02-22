def fibo(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a+b
n = int(input().strip())
first = True
for x in fibo(n):
    if not first:
        print(",", end="")
    print(x, end="")
    first = False
