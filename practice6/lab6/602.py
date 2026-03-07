n = int(input())
a = list(map(int, input().split()))
r = list(filter(lambda x: x % 2 == 0, a))
print(len(r))