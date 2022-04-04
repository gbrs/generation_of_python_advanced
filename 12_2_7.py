'''слишком сложно решил: просто зашафлить исходный список и вывести пары.
нулевой с первым, первый - со вторым...'''

from random import shuffle
lst = [input() for i in range(int(input()))]
while True:
    lst_2 = lst[:]
    shuffle(lst_2)
    # насколько это ужасно наугад перемешивать ожидая, что ни одна пара не совпадет?
    if all([lst[i] != lst_2[i] for i in range(len(lst))]):
        break

for pair in zip(lst, lst_2):
    print(f'{pair[0]} - {pair[1]}')
