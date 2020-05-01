import random

numbers = []

for i in range(100):
    numbers.append(random.randint(0, 100))
print(numbers)
# проверить есть ли 25 в списке
if 25 in numbers:
    print('25 есть в списке')
else:
    print('нет числа')

print('25 есть в списке') if 25 in numbers else print('нет числа')

result = None
if 4 in numbers:
    result = 'Есть число'
else:
    result = 'нет числа'
print('Результат выражения:', result)

result = 'Есть число' if 4 in numbers else 'нет числа'

print('Результат выражения:', result)

# Генераторы
