n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
r = []
for x, y in zip(a,b):
    r.append(x*y)

print(sum(r))