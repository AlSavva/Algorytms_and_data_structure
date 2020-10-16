# Написать программу сложения и умножения двух шестнадцатеричных чисел. При
# этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import OrderedDict, deque

stg = '0123456789ABCDEF'
my_dict = {}
for i in range(16):
    my_dict[stg[i]] = i


def in_hex(num):
    res = deque()
    while num > 0:
        for key, value in my_dict.items():
            if value == num % 16:
                res.appendleft(key)
        num //= 16
    return res


def in_dec(lst):
    ln = len(lst) - 1
    decnum = 0
    for el in lst:
        decnum += my_dict[el] * 16 ** ln
        ln -= 1
    return decnum


hexnum1 = list(input('Введите первое шестнадцатиричное число: ').upper())
print(f'Введено: {hexnum1}')
hexnum2 = list(input('Введите второе шестнадцатиричное число: ').upper())
print(f'Введено: {hexnum1}')
print(f" {''.join(hexnum1)} + {''.join(hexnum2)} = "
      f"{''.join(in_hex(in_dec(hexnum1) + in_dec(hexnum2)))}")
print(f'Результат сложения: {in_hex(in_dec(hexnum1) + in_dec(hexnum2))}')
print(f" {''.join(hexnum1)} * {''.join(hexnum2)} = "
      f"{''.join(in_hex(in_dec(hexnum1) * in_dec(hexnum2)))}")
print(f'Результат умножения: {in_hex(in_dec(hexnum1) * in_dec(hexnum2))}')
