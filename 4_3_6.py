def chunked(lst, size):
    answer = []
    for i in range(0, len(lst), size):
        answer.append(lst[i:i + size])
    return answer


lst = input().split()
size = int(input())

print(chunked(lst, size))
