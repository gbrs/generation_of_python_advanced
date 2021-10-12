# s = '0000a00o0n00t00000o000000n'.lower()

anton = 'anton'

for i in range(int(input())):
    s = input().lower()
    k = start = 0
    for j in range(len(s)):
        place = s.find(anton[k], start)
        if place != -1:
            start = place
            k += 1
            if k == 5:
                print(i + 1)
                break


