def matrix(x=1, y=None, v=0):
    if y is None:
        y = x
    return [[v] * y for _ in range(x)]


print(matrix())         # матрица 1 × 1 из 0
print(matrix(3))        # матрица 3 × 3 из 0
print(matrix(2, 5))     # матрица 2 × 5 из 0
print(matrix(3, 4, 9))  # матрица 3 × 4 из 9
