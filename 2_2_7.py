t = input()
r = input()
t = 2 if t == 'бумага' else 1 if t == 'камень' else 0
r = 2 if r == 'бумага' else 1 if r == 'камень' else 0

print(('ничья', 'Тимур', 'Руслан')[t - r])

'''
чье-то решение:
s = ['камень', 'ножницы', 'бумага']
print(['ничья', 'Руслан', 'Тимур'][s.index(input()) - s.index(input())])
'''
