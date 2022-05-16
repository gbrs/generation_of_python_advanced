dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {char: (dict1.get(char, 0) + dict2.get(char, 0))
          for char in set(dict1.keys()) | set(dict2.keys())}  # сеты не обязательны были
print(result)
