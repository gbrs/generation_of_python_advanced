lst = input().split()
answer = []
dct = {}
for word in lst:
    if dct.get(word, 0):
        answer.append('_'.join((word, str(dct[word]))))
        dct[word] = dct[word] + 1
    else:
        answer.append(word)
        dct[word] = 1
print(*answer)
