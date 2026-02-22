def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    d = 3
    while d * d <= x:
        if x % d == 0:
            return False
        d += 2
    return True

def primes(n):
    for x in range(2, n + 1):
        if is_prime(x):
            yield x

n = int(input().strip())

first = True
for p in primes(n):
    if not first:
        print(" ", end="")
    print(p, end="")
    first = False
