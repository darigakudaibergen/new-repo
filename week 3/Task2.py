import math

def area_triangle(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def main():
    a = float(input())
    print(6 * area_triangle(a, a, a))
    
    for _ in range(3):
        x = float(input())
        y = float(input())
        print(x * y)

main()