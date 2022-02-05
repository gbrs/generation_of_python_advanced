"""
Поиск значения числа пи.
Монте-Карлим. Тыкаем точки в квадрат 2 х 2 и вписанный в него круг.
S = pi * R**2
"""

import random


n = 10 ** 6

cnt_in_figure = 0
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        cnt_in_figure += 1
circle_square = cnt_in_figure / n * 4
pi = circle_square / 1**2
print(pi)
