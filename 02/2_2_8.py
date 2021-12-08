dct = {'ножницы': 0, 'бумага': 1, 'камень': 2, 'ящерица': 3, 'Спок': 4}
diff = (dct[input()] - dct[input()]) % 5

print('ничья' if diff == 0 else 'Тимур' if diff in (2, 4) else 'Руслан')
