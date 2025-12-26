import sys
from collections import Counter

data = sys.stdin.read().split()
if not data:
    sys.exit()

cnt = Counter(data)

most_popular = cnt.most_common(1)[0][0]
once = [item for item in cnt if cnt[item] == 1]
sorted_items = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

print("Purchase frequency:")
for item, count in cnt.items():
    print(f"{item}: {count}")

print(f"Most popular item: {most_popular}")
print("Purchased once:", " ".join(once))

print("Sorted by frequency:")
for item, count in sorted_items:
    print(f"{item} {count}")
