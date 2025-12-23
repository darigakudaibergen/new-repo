import sys

def main():
    s = sys.stdin.readline().strip()
    cnt = 0
    for i in range(len(s) - 4):
        sub = s[i:i+5]
        if sub == ">>-->" or sub == "<--<<":
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()
