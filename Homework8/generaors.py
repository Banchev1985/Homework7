numbers = [1, 2, 5, 8, 7, 3, 9, 100, 256]
import random

result = []
for number in numbers:
    if 5 < number < 50:
        result.append(number)
print(result)

result = filter(lambda number: 5 < number < 50, numbers)
print(list(result))

result = [number for number in numbers if 5 < number < 50]
print(result)

names = ['leo', 'kate', 'max', 'mag']

name_upper = [name.upper() for name in names]
print(name_upper)

names_m = [name for name in names if name[0] == 'm']
print(names_m)
names_m = [name for name in names if name.startswith('m')]
print(names_m)

numbers = [1, 2, 5, 8, 7, 3, 9, 100, 256]

result = [1 if number > 5 else 0 for number in numbers]
print(result)

result = {random.randint(1, 100) for i in range(100)}
print(result)

result = {name: len(name) for name in names}
print(result)
