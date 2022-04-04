lst = input().split()
s1, s2, s3 = map(set, lst)
print('YES' if s1 == s2 == s3 else 'NO')
