from random import choice


def generate_password(length):
    s = ''
    for _ in range(length):
        s = ''.join([s, choice(lst)])
    return s


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))


lst = [chr(i) for i in range(ord('a'), ord('z') + 1)] \
      + [chr(i) for i in range(ord('A'), ord('Z') + 1)] \
      + list(map(str, range(0, 10)))
for char in ('o', 'O', '0', 'l', 'I', '1'):
    lst.remove(char)

n, m = int(input()), int(input())
generate_passwords(n, m)
