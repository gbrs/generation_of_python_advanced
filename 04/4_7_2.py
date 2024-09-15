n, m = map(int, input().split())
m1 = [[int(x) for x in input().split()] for i in range(n)]

input()

m, k = map(int, input().split())
m2 = [[int(x) for x in input().split()] for i in range(m)]

m3 = [[0] * k for i in range(n)]

for i in range(n):
    for j in range(k):
        sm = 0
        for p in range(m):
            sm += m1[i][p] * m2[p][j]
        m3[i][j] = sm

[print(*row) for row in m3]
