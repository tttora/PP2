n = int(input())
a = list(map(int, input().split()))
r = list(map(lambda x: x**2, a))
print(sum(r))