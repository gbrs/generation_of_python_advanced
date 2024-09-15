"""
Поиск площади фигуры методом Монте-Карло. Тыкаем точки в квадрат 4 х 4 и вписанную в него фигуру.
"""

import random

n = 10 ** 6

cnt_in_figure = 0
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if (-2 <= x <= 2 and
            -2 <= y <= 2 and
            x ** 3 + y ** 4 + 2 >= 0 and
            3 * x + y ** 2 <= 2):
        cnt_in_figure += 1
print(cnt_in_figure / n * 16)
