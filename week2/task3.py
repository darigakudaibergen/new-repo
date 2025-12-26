s = input().strip()

a = s[0]
op = s[1]
b = s[2]
c = s[4]

if a == 'x':
    B = int(b)
    C = int(c)
    if op == '+':
        x = C - B
    else:
        x = C + B

elif b == 'x':
    A = int(a)
    C = int(c)
    if op == '+':
        x = C - A
    else:
        x = A - C

else:  # c == 'x'
    A = int(a)
    B = int(b)
    if op == '+':
        x = A + B
    else:
        x = A - B

print(x)
