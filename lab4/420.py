m = int(input().strip())

g = 0          # global variable
n = 0          # outer's variable
local_sum = 0  # inner local variable (only exists inside inner)

for _ in range(m):
    scope, val = input().split()
    val = int(val)

    if scope == "global":
        g += val
    elif scope == "nonlocal":
        n += val
    else:  # "local"
        local_sum += val

print(g, n)
