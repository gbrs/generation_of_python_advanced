s = input() + ' запретил букву'
for i in range(ord('а'), ord('я') + 1):
    if chr(i) in s:
        print(s + ' ' + chr(i))
        s = s.replace(chr(i), '').strip()
