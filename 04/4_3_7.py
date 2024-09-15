lst = input().split()
answer = [[]]
for sub_str_len in range(1, len(lst) + 1):
    for i in range(len(lst) - sub_str_len + 1):
        new_variant = []
        for j in range(sub_str_len):
            new_variant.append(lst[i + j])
        answer.append(new_variant)
print(answer)
