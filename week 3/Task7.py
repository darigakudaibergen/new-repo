def main():
    x = float(input())
    y = float(input())
    z = float(input())
    t = float(input())
    area1 = 0.5 * x * y
    area2 = 0.5 * z * t
    print(area1 + area2)
    
    n = int(input())
    octal = oct(n)[2:]
    print(octal.zfill(10))

main()