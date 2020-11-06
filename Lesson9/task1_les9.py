# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных
# подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой
# другой из модуля hashlib задача считается не решённой.

import hashlib


def subs_count(s: str) -> int:
    tot_subs = set()
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if len(s[i:j]) != len(s):
                tot_subs.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
    return len(tot_subs)


string = input('Enter string: ')
print(
    f'Number of different substring in string "{string}": {subs_count(string)}')
