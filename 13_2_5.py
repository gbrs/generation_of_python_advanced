from fractions import Fraction

result = Fraction(0)
for i in range(int(input())):
    result += Fraction(1, (i + 1)**2)

print(result)
