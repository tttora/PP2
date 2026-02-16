n = int(input())

names = {}
for i in range(n):
    s, k = input().split()
    k = int(k)

    if s in names:
        names[s] += k
    else:
        names[s] = k

for name in sorted(names):
    print(name, names[name])
