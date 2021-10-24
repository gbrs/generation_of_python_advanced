from itertools import combinations
lst = [int(input()) for i in range(int(input()))]
v = int(input())
print('ДА' if any(pair[0] * pair[1] == v for pair in combinations(lst, 2)) else 'НЕТ')
