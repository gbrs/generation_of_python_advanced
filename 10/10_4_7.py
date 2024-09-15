word = input()
n = int(input())

dct = {}
for _ in range(n):
    value, key = input().split(': ')
    dct[int(key)] = value

for char in set(word):
    frequency = word.count(char)
    word = word.replace(char, dct[frequency])

print(word)
