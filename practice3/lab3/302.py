def isUsual(n):
    if n <= 0:
        return False
    for i in (2,3,5):
        while n % i == 0:
            n //= i
    if n == 1:
        return True
    else:
        return False

num = int(input())

if isUsual(num):
    print("Yes")
else:
    print("No")