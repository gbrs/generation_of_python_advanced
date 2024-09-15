dct = {}

for _ in range(int(input())):
    tel, name = input().lower().split()
    dct.setdefault(name, []).append(tel)

for _ in range(int(input())):
    tels = dct.get(input().lower(), [])
    if tels:
        print(*tels)
    else:
        print('абонент не найден')
