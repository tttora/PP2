import math

R = float(input().strip())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

A = (x1, y1)
B = (x2, y2)

dx = x2 - x1
dy = y2 - y1
seg_len = math.hypot(dx, dy)

# If same point
if seg_len == 0.0:
    print(f"{0.0:.10f}")
    raise SystemExit

# Check if straight segment intersects the *interior* of the circle
dd = dx * dx + dy * dy
u = -(x1 * dx + y1 * dy) / dd
if u < 0.0:
    cx, cy = x1, y1
elif u > 1.0:
    cx, cy = x2, y2
else:
    cx, cy = x1 + u * dx, y1 + u * dy

min_dist2 = cx * cx + cy * cy
R2 = R * R
eps = 1e-12

if min_dist2 >= R2 - eps:
    print(f"{seg_len:.10f}")
    raise SystemExit

# Need to go around the circle with tangents + arc
d1 = math.hypot(x1, y1)
d2 = math.hypot(x2, y2)

# Tangent lengths (0 if on circle)
t1 = math.sqrt(max(0.0, d1 * d1 - R2))
t2 = math.sqrt(max(0.0, d2 * d2 - R2))

angA = math.atan2(y1, x1)
angB = math.atan2(y2, x2)

# Angle between OA and OT (to tangent point)
beta1 = math.acos(max(-1.0, min(1.0, R / d1))) if d1 > R else 0.0
beta2 = math.acos(max(-1.0, min(1.0, R / d2))) if d2 > R else 0.0

two_pi = 2.0 * math.pi

def mod2pi(a):
    a %= two_pi
    if a < 0:
        a += two_pi
    return a

best = float("inf")
for s in (1.0, -1.0):
    tA = angA + s * beta1
    tB = angB - s * beta2
    arc_angle = mod2pi(tB - tA)
    best = min(best, t1 + t2 + R * arc_angle)

print(f"{best:.10f}")
