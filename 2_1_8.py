lst = [i for i in range(1, int(input()) + 1)]
k = int(input())

start = -1
while len(lst) > 1:
    place = (start + k) % len(lst)
    lst.pop(place)
    start = place - 1

print(*lst)
