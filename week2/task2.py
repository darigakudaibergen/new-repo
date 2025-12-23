import sys

def main():
    a = sys.stdin.readline().rstrip("\n")
    b = sys.stdin.readline().rstrip("\n")
    n, m = len(a), len(b)

    rotations = set()
    bb = b + b
    for i in range(m):
        rotations.add(bb[i:i+m])

    ans = 0
    for i in range(n - m + 1):
        if a[i:i+m] in rotations:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
