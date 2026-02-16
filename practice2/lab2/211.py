n, l, r = map(int, input().split())
list1 = list(map(int, input().split()))
l = l-1
r = r-1
list1[l:r+1] = list1[l:r+1][::-1]
for i in range(n):
    print(list1[i], end=' ')