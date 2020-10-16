# Задача: программа будет хранить значения ай-пи адреса и порта по умолчанию,
# при этом пользовательб призапуске через консоль может передать новый адрес,
# или порт. Будем анализировать ввел данные пользователь, или не ввел, и выби
# рать, какое значение использовать, по умолчанию, или введенное.

import argparse # модуль позволяет работать с ключами в командной строке.
from collections import ChainMap


defaults = {'ip': 'localhost', 'port': 7777}
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip') # добавляем в парсер необходимые ключи
parser.add_argument('-p', '--port')
# попросим проанализировать строку запуска из консоли, и сохраним результат в
# отдельный словарь
args = parser.parse_args()
new_dict = {key: value for key, value in vars(args).items() if value}
# при запуске этого скрипта из консоли (python exsample1.py --port 8088)
# пользователь введет ключи и значения,
# благодаря функции vars(), мы сохраним ключи и значения в соотв. переменные.
# проверим есть ли value, и если есть, добавим пару в словарь
settings = ChainMap(new_dict, defaults)
print(settings['ip'])
print(settings['port'])