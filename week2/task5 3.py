import sys

ALLOWED = set("ABCEHKMOPTXY")

def is_valid(x: str) -> bool:
    if len(x) != 6:
        return False
    if x[0] not in ALLOWED:
        return False
    if not (x[1].isdigit() and x[2].isdigit() and x[3].isdigit()):
        return False
    if x[4] not in ALLOWED or x[5] not in ALLOWED:
        return False
    return True

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    for i in range(1, n + 1):
        line = data[i].strip()
        print("Yes" if is_valid(line) else "No")

if __name__ == "__main__":
    main()
