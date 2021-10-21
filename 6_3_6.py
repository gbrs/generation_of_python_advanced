lst = [input().split() for _ in range(int(input()))]
[print(*i) for i in lst]
print()
for i in lst:
    if i[1] in ('4', '5'):
        print(*i)
