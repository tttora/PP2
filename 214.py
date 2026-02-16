n = int(input())
arr = list(map(int, input().split()))

max_count = 0
result = None

for x in arr:
    count = arr.count(x)
    if count > max_count:
        max_count = count
        result = x
    elif count == max_count:
        if x < result:
            result = x

print(result)
