n = int(input())
a = list(map(int, input().split()))
r = all(x >= 0 for x in a)
if r:
    print("Yes")
else:
    print("No")