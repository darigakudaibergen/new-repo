def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def point_in_circle(px, py, cx, cy, r):
    return (px - cx) ** 2 + (py - cy) ** 2 < r * r

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    num = a * d
    den = b * c
    g = gcd(num, den)
    print(num // g, den // g)
    
    cx = float(input())
    cy = float(input())
    r = float(input())
    
    p1 = float(input())
    p2 = float(input())
    f1 = float(input())
    f2 = float(input())
    l1 = float(input())
    l2 = float(input())
    
    count = 0
    if point_in_circle(p1, p2, cx, cy, r):
        count += 1
    if point_in_circle(f1, f2, cx, cy, r):
        count += 1
    if point_in_circle(l1, l2, cx, cy, r):
        count += 1
    print(count)

main()