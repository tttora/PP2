n = int(input())
nums = list(map(int,input().split()))
pos = 0
for i in range(n):
    if nums[i] > 0:
        pos = pos + 1

print(pos)