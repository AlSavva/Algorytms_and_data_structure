# В программе генерируется случайное целое число от 0 до 100. Пользователь
# должен его отгадать не более чем за 10 попыток. После каждой неудачной
# попытки должно сообщаться, больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

from random import randint

n = randint(0, 100)
m = int(input('Введите число от 0 до 100: '))
i = 1
while i < 10:
    if m == n:
        print(f'Вы угадали! Количество попыток - {i}.')
        break
    elif m < n:
        print('Выше число меньше.')
    else:
        print('Ваше число больше.')
    m = int(input('Еще одна попытка. Введите число от 0 до 100: '))
    i += 1
else:
    print(f'Увы! За 10 попыток вы не угадали число {n}')