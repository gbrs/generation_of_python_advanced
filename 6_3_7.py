n = int(input())

a = b = c = 1

[print(1, end=' ') for i in range(min(3, n))]

for i in range(n-3):
    a, b, c = b, c, a + b + c
print(c, end=' ')
