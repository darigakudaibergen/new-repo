a = input().strip()
b = input().strip()

m = len(b)
bb = b + b

rotations = set()
for i in range(m):
    rotations.add(bb[i:i+m])

ans = 0
for i in range(len(a) - m + 1):
    if a[i:i+m] in rotations:
        ans += 1

print(ans)
