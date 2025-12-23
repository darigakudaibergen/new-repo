import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    seen = set()
    for i in range(n - m + 1):
        seen.add(s[i:i+m])

    print(len(seen))

if __name__ == "__main__":
    main()
