import math

def area_circle(r):
    return math.pi * r * r

def area_rectangle(a, b):
    return a * b

def area_square(a):
    return a * a

def area_triangle(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def main():
    print("1) Circle  2) Rectangle  3) Square  4) Triangle")
    k = int(input())
    
    if k == 1:
        r = float(input())
        print(area_circle(r))
    elif k == 2:
        a = float(input())
        b = float(input())
        print(area_rectangle(a, b))
    elif k == 3:
        a = float(input())
        print(area_square(a))
    elif k == 4:
        a = float(input())
        b = float(input())
        c = float(input())
        print(area_triangle(a, b, c))
    
    for _ in range(3):
        arr = list(map(int, input().split()))
        s = sum(arr)
        print(s, s / len(arr))

main()