s = set()
for _ in range(3):
    s = s.union(map(int, input().split()))
answer = sorted(set(range(0, 10 + 1)) - s)
print(*answer)
