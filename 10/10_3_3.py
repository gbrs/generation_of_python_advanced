# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# # result = {char: text.count(char) for char in set(text)}
# result = {}
# for char in text:
#     result[char] = result.get(char, 0) + 1
# print(result)
from collections import Counter
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = Counter(text)
print(type(result))
