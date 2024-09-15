n = int(input())
dct = {}

for _ in range(n):
    lst = list(input().split())
    for i in range(1, len(lst)):
        dct[lst[i]] = lst[0]

m = int(input())
for _ in range(m):
    print(dct[input()])
