n, m = 2, 3
lst = [[None] * m for _ in range(n)]
# print(lst)
cnt = 1109
top = 0
bottom = n
left = -1
right = m


while True:

    right -= 1
    if left < right:
        for i in range(left, right):
            cnt += 1
            lst[top][i] = cnt
        [print(*row) for row in lst]
        print()
    else:
        cnt += 1
        lst[top][right] = cnt
        break

    bottom -= 1
    if top < bottom:
        for i in range(top, bottom):
            cnt += 1
            lst[i][right] = cnt
        [print(*row) for row in lst]
        print()
    else:
        cnt += 1
        lst[bottom][right] = cnt
        break

    left += 1
    if left < right:
        for i in range(right, left, -1):
            cnt += 1
            lst[bottom][i] = cnt
        [print(*row) for row in lst]
        print()
    else:
        cnt += 1
        lst[bottom][left] = cnt
        break

    top += 1
    if top < bottom:
        for i in range(bottom, top, -1):
            cnt += 1
            lst[i][left] = cnt
        [print(*row) for row in lst]
        print()
    else:
        cnt += 1
        lst[top][left] = cnt
        break

[print(*row) for row in lst]
