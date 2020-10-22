import sys


# Вариант 1: Функция подсчёта памяти на все переменные в коде:
def var_memory(objects, verbose=True):
    tot_mem = 0
    for item in objects:
        if item.startswith('__'):
            # убираем magic methods
            continue
        elif hasattr(objects[item], '__call__'):
            # исключаем функции
            continue
        elif hasattr(objects[item], '__loader__'):
            # исключаем модули
            continue
        else:
            tot_mem += sys.getsizeof(objects[item])
            if verbose:
                print(f'Переменная= {item};\tТип= {type(objects[item])};\t'
                      f'Значение= {objects[item]};\tЗанимает'
                      f' {sys.getsizeof(objects[item])} байт(а).')
    return f'Все переменные заняли {tot_mem} байт(а).'
