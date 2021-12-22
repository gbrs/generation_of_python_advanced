s = '''CS101	3004	Хайнс	8:00
CS102	4501	Альварадо	9:00
CS103	6755	Рич	10:00
NT110	1244	Берк	11:00
CM241	1411	Ли	13:00'''

s = [string.split() for string in s.split('\n')]
print(s)
d = {lst[0]: lst[1:] for lst in s}
key = input()
print(f'{key}: {d[key][0]}, {d[key][1]}, {d[key][2]}')
