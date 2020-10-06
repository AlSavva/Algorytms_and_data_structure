# Определить, какое число в массиве встречается чаще всего.

def gen_list(n, m, l):
    """Функция генерирует список заданной длинны l из случайных целых чисел в
    диапазоне от n до m."""
    from random import randint
    return [randint(n, m) for _ in range(l)]


my_list = gen_list(1, 10, 25)
print(my_list)
count = ioften = 0
mymax = 0
for i in range(len(my_list) - 1):
    for j in range(i, len(my_list)):
        if my_list[i] == my_list[j]:
            count += 1
        if count > mymax:
            mymax = count
            ioften = i
    count = 0
print(f'Число {my_list[ioften]} встречается в списке {max} раз.'
      if mymax > 1 else f'В списке нет повторяющихся элементов.')
