n, m = map(int, input().split())

m1 = [[int(x) for x in input().split()] for i in range(n)]
input()
m2 = [[int(x) for x in input().split()] for i in range(n)]


m3 = [[(m1[i][j] + m2[i][j]) for j in range(m)]for i in range(n)]

[print(*row) for row in m3]
