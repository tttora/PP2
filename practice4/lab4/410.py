def cycle(arr, n):
    for i in range(0,n):
        for j in arr:
            yield j

arr = input().split()
n = int(input().strip())

for x in cycle(arr, n):
    print(x, end=" ")