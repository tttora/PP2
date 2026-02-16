n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
list1.reverse()
for i in range(n):
    print(list1[i], end=" ")