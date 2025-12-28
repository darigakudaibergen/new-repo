def satisfies(n):
    original = n
    while n > 0:
        digit = n % 10
        if digit == 0 or original % digit != 0:
            return False
        n //= 10
    return True

def swap_first_last(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]

def main():
    n = int(input())
    result = []
    for i in range(1, n + 1):
        if satisfies(i):
            result.append(str(i))
    print(' '.join(result))
    
    m = int(input())
    A = list(map(int, input().split()))
    print(' '.join(map(str, A)))
    swap_first_last(A)
    print(' '.join(map(str, A)))

main()