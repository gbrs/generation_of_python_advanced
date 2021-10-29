"""
заполнение матрицы со смещением
"""


n, m = [int(i) for i in input().split()]
lst = [[None] * m for _ in range(n)]

cnt = 1

for i in range(n):
    for j in range(m):
        # начинаю заполнять с элемента (j - i). % m - для n > m
        lst[i][(j - i) % m] = cnt
        cnt += 1
    cnt = 1

[print(*row) for row in lst]
