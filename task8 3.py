import sys
from collections import Counter

def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    print("YES" if Counter(s1) == Counter(s2) else "NO")

if __name__ == "__main__":
    main()
