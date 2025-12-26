n = int(input())
allowed = set("ABCEHKMOPTXY")

for _ in range(n):
    s = input().strip()
    if (len(s) == 6 and 
        s[0] in allowed and 
        s[1:4].isdigit() and 
        s[4] in allowed and 
        s[5] in allowed):
        print("Yes")
    else:
        print("No")
