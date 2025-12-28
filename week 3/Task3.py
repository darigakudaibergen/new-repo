import math

def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)

def main():
    a1 = float(input())
    b1 = float(input())
    a2 = float(input())
    b2 = float(input())
    h1 = hypotenuse(a1, b1)
    h2 = hypotenuse(a2, b2)
    if h1 > h2:
        print("First hypotenuse is greater")
    elif h1 < h2:
        print("Second hypotenuse is greater")
    else:
        print("Hypotenuses are equal")
    
    s = input()
    words = s.split()
    result = []
    for word in words:
        result.append(''.join(sorted(word)))
    print(' '.join(result))

main()