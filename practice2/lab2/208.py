n = int(input())
for i in range(0,100):
    s = 2**i
    if(s <= n):
        print(s, end=" ")