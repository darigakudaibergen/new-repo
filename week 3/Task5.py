def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    num = a * d - b * c
    den = b * d
    if num == 0:
        print(0, 1)
    else:
        g = gcd(abs(num), den)
        print(num // g, den // g)
    
    n = int(input())
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(str(i))
    print(' '.join(divisors))

main()