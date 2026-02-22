x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# Reflect B over Ox
y2p = -y2

# Line from A(x1,y1) to B'(x2,y2p): A + t*(B'-A)
dy = y2p - y1

# Find t where y = 0: y1 + t*dy = 0
t = -y1 / dy

x = x1 + t * (x2 - x1)
print(f"{x:.10f} 0.0000000000")
