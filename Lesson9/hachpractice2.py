# задача №2 поиск подстроки в строке:
# алгоритм Рабина-Карпа
import hashlib


def rabin_karp(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'String`s cannot be empty!!!'
    assert len(s) >= len(subs), 'string cannot be shorter than a substring'
    len_sub = len(subs)
    h_sub = hashlib.sha1(subs.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_sub == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            if s[i:i + len_sub] == subs:
                return i
    return -1


s_1 = input('Enter string: ')
s_2 = input('Enter substring: ')
pos = rabin_karp(s_1, s_2)
print(
    f'Substring found in position {pos}' if pos != -1 else 'Substring not found')
