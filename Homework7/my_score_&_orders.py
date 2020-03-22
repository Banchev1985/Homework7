import os
import re

FILE_NAME = 'score.txt'
FILE_ORDERS = 'orders.txt'
scores = 0
purchase = []
# if os.path.exists(FILE_NAME):
#     with open(FILE_NAME, 'r') as f:
#         scores = f.read()

while True:
    print('0. проверить счет')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '0':
        # Проверяем сколько денег на счету из файла
        with open(FILE_NAME, 'r') as f:
            result = f.read()
            # new_result = int(result)
            print(f'У Вас счете {result}')
    elif choice == '1':
        scores = int(input('На сколько пополнить счет?: '))
        # Пополняем счет, плюсуем дополнительную сумму к имеющейся, записанной в файле
        with open(FILE_NAME, 'r') as f:
            money = f.read()  # читаем файл
            my_money = int(money)
            new_score = scores + my_money  # суммируем числа
            print(new_score)
        with open(FILE_NAME, 'w') as f:
            f.write(f'{new_score}\n')  # записываем результат

    elif choice == '2':
        purchase_question_score = int(input('На какую суммы Вы хотите сделать покупку?: '))
        # Читаем из файла значение счета, и сравниваем с суммой покупки
        with open(FILE_NAME, 'r') as f:
            money = f.read()
            my_money = int(money)
        if my_money == '':
            print('У Вас нет средств на счете\nПополните свой счет')
        elif my_money < purchase_question_score:
            print('У Вас недостаточно средств на счете')
        else:
            with open(FILE_NAME, 'w') as f:
                finaly_score = my_money - purchase_question_score
                f.write(f'{finaly_score}\n')
            purchase_question = input('Что вы хотите купить?: ')
            purchase.append(purchase_question)
            with open('orders.txt', 'a') as f:
                f.write(f'{purchase}\n')
                print(purchase)
                print(finaly_score)
    elif choice == '3':
        with open(FILE_ORDERS, 'r') as f:
            orders = f.read()
            my_orders = str(orders)

        print('Вы купили\n', my_orders)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
