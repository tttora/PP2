n = int(input())
list1 = list(map(int, input().split()))
for i in range(n):
    print(list1[i]**2, end=' ')