n = int(input())
nums = list(map(int,input().split()))
max = -999999
maxindex = -1
for i in range(n):
    if nums[i] > max:
        max = nums[i]
        maxindex = i+1
print(maxindex)