"""
Напишите программу, которая возводит квадратную матрицу в m-ую степень.
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы построчно через пробел, затем натуральное число mm.
"""


import copy

n = int(input())
# ввод матрицы
arr1 = [[int(x) for x in input().split()] for i in range(n)]

# создаем служебные промежуточные матрицы
arr2 = copy.deepcopy(arr1)
arr3 = copy.deepcopy(arr2)
# print(arr3)
m = int(input())

# возведение в степень
for _ in range(m - 1):
    # перебор элементов
    for i in range(n):
        for j in range(n):
            sm = 0
            # суммирование произведения вектор-столбца на вектор-строку
            for p in range(n):
                sm += arr2[i][p] * arr1[p][j]
            arr3[i][j] = sm
    arr2 = copy.deepcopy(arr3)

[print(*row) for row in arr3]
