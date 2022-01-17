import random

length = int(input())    # длина пароля

lst = list(range(ord('a'), ord('z') + 1)) + list(range(ord('A'), ord('Z') + 1))
[print(chr(random.choice(lst)), end='') for _ in range(length)]
