st = set('0123456789')
for i in range(int(input())):
    st = st & set(input())
print(*sorted(st))
