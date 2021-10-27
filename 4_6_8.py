"""
заполнение змейкой матрицы n на m
"""


n, m = [int(i) for i in input().split()]
lst = [[None] * m for _ in range(n)]

cnt = 1

for i in range(n):
    for j in range(m):
        # нечетные строки заполняем от конца к началу
        if i % 2:
            lst[i][m - 1 - j] = cnt
        else:
            lst[i][j] = cnt
        cnt += 1

[print(*row) for row in lst]
