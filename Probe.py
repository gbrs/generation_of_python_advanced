words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry',
         'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon',
         'currant', 'Almond']
print(*sorted(set(i.lower()[0] for i in words)))
s = '''CS101	3004	Хайнс	8:00
CS102	4501	Альварадо	9:00
CS103	6755	Рич	10:00
NT110	1244	Берк	11:00
CM241	1411	Ли	13:00'''