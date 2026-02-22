import math

R = float(input().strip())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1
seg_len = math.hypot(dx, dy)

# Degenerate segment (a single point)
if seg_len == 0.0:
    inside = (x1 * x1 + y1 * y1) <= R * R + 1e-12
    print(f"{0.0:.10f}")
    raise SystemExit

A = dx * dx + dy * dy
B = 2.0 * (x1 * dx + y1 * dy)
C = x1 * x1 + y1 * y1 - R * R

disc = B * B - 4.0 * A * C

if disc < -1e-12:
    # No intersections with the circle
    if x1 * x1 + y1 * y1 <= R * R + 1e-12:
        print(f"{seg_len:.10f}")
    else:
        print(f"{0.0:.10f}")
else:
    if disc < 0.0:
        disc = 0.0
    sqrt_disc = math.sqrt(disc)

    t1 = (-B - sqrt_disc) / (2.0 * A)
    t2 = (-B + sqrt_disc) / (2.0 * A)
    if t1 > t2:
        t1, t2 = t2, t1

    lo = max(0.0, t1)
    hi = min(1.0, t2)

    if hi <= lo:
        print(f"{0.0:.10f}")
    else:
        print(f"{seg_len * (hi - lo):.10f}")
