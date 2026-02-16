import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)

    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]

    q = int(next(it))

    for _ in range(q):
        op = next(it)
        if op == "add":
            x = int(next(it))
            arr = list(map(lambda a, x=x: a + x, arr))
        elif op == "multiply":
            x = int(next(it))
            arr = list(map(lambda a, x=x: a * x, arr))
        elif op == "power":
            x = int(next(it))
            arr = list(map(lambda a, x=x: a ** x, arr))
        else:  
            arr = list(map(lambda a: abs(a), arr))

    sys.stdout.write(" ".join(map(str, arr)))

if __name__ == "__main__":
    main()
