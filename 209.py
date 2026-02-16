n = int(input())
nums = list(map(int,input().split()))
mx = -999999
mn = 999999
for i in range(n):
    if nums[i] > mx:
        mx = nums[i]
    if nums[i] < mn:
        mn = nums[i]
for i in range(n):
    if(nums[i] == mx):
        nums[i] = mn
for i in range(n):
    print(nums[i], end = " ")