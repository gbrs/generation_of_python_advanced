s = input()
insertion_place = -4
for _ in range((len(s) - 1) // 3):
    s = ''.join((s[:insertion_place + 1], ',', s[insertion_place + 1:]))
    insertion_place -= 4
print(s)
