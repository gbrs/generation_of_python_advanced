s = '''00 на zero;
11 на one;
22 на two;
33 на three;
44 на four;
55 на five;
66 на six;
77 на seven;
88 на eight;
99 на nine.'''

s = [string.split() for string in s.split('\n')]
print(s)
d = {lst[0][0]: lst[-1][:-1] for lst in s}
print(*[d[digit] for digit in input()])

