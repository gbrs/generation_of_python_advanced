# исходное описание кодировки с сайта
code_string = '''1	.,?!:
2	ABC
3	DEF
4	GHI
5	JKL
6	MNO
7	PQRS
8	TUV
9	WXYZ
0	space (пробел)'''
# разбираем исходное описание в список
lst = [string.split() for string in code_string.split('\n')]
# заменяем плохо обработанную последнюю строку
lst[-1] = ['0', ' ']

# генерим словарь "ключ: (кнопка, количество повторов)"
code_dict = {}
for item in lst:
    for serial_number, char in enumerate(item[1]):
        code_dict[char] = (item[0], serial_number + 1)

# генерим ответ на вводимую строку
s = input()
answer = []
for char in s:
    dict_response = code_dict.get(char.upper(), ('', 0))  # если нет знака в словаре, то печатаем 0 раз ничего
    answer.append(dict_response[0] * dict_response[1])
print(*answer, sep='')
