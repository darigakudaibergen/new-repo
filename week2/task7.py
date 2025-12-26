import sys
from collections import Counter

items = sys.stdin.read().split()
cnt = Counter(items)

most_popular = cnt.most_common(1)[0][0]
once = [item for item, c in cnt.items() if c == 1]
sorted_items = cnt.most_common()

print("Purchase frequency:")
for item, c in cnt.items():
    print(f"{item}: {c}")

print(f"Most popular item: {most_popular}")
print("Purchased once:", " ".join(once))

print("Sorted by frequency:")
for item, c in sorted_items:
    print(f"{item} {c}")
