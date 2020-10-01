# Сформировать из введенного числа обратное по порядку входящих в него цифр и
# вывести на экран. Например, если введено число 3486, надо вывести 6843

def str_numreverse(n):
    if n // 10 < 1:
        return str(n)
    return str(n % 10) + str_numreverse(n // 10)


num = int(input('Введите число: '))
print(str_numreverse(num))
