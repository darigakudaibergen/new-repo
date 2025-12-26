n, m = map(int, input().split())
text = input().strip()

words = set()
for i in range(len(text) - m + 1):
    words.add(text[i:i+m])

print(len(words))
