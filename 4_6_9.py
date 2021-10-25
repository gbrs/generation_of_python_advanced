"""
заполнение диагоналями матрицы n на m
"""


# генерация исходного списка
n, m = [int(i) for i in input().split()]
lst = [[None] * m for _ in range(n)]

# счетчик, который будет давать нам числа, которыми мы заполняем таблицу
cnt = 1

# у диагоналей одинаковые суммы индексов: от 0 до n + m - 2
for i in range(n + m - 1):
    # начальные позиции заполнения диагоналей
    col = i if i < m else m - 1
    row = 0 if i < m else i - m + 1
    # заполняем побочную диагональ пока не упремся в левую или нижнюю границу
    while col > -1 and row < n:
        lst[row][col] = cnt
        cnt += 1
        col -= 1
        row += 1

[print(*row) for row in lst]
