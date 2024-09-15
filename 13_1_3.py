from decimal import Decimal
num = Decimal(input())

lst = [int(s) for s in str(num) if s.isdigit()]
print(min(lst) + max(lst))
