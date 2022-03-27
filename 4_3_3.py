def pascal(cnt=1, lst=[1, 1]):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    else:
        while cnt < n:
            lst_output = [1]
            for i in range(cnt):
                lst_output.append(lst[i] + lst[i + 1])
            lst_output.append(1)
            cnt += 1
            return pascal(cnt, lst_output)
    return lst


n = int(input())
print(pascal())
