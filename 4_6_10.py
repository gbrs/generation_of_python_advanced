"""
заполнение спиралью матрицы n на m
"""

n, m = 4, 6
lst = [[None] * m for _ in range(n)]
# print(lst)
cnt = 0
top = 0
bottom = n - 1
left = 0
right = m - 1


while top <= bottom and left <= right:
    for i in range(left, right):
        cnt += 1
        lst[top][i] = cnt
    top += 1
    while top <= bottom and left <= right:
        for i in range(top - 1, bottom):
            cnt += 1
            lst[i][right] = cnt
        left += 1








[print(*row) for row in lst]
