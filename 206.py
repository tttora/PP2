n = int(input())
nums = list(map(int,input().split()))
max = -999999
for i in range(n):
    if nums[i] > max:
        max = nums[i]

print(max)