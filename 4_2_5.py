list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

for lst in list1:
    counter += len(lst)
    total += sum(lst)

print(total / counter)
