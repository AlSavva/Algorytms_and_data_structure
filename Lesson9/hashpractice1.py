# задача №1 сравнение строк с помощью хэширования:
import hashlib


def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a)>0 and len(b)>0, 'String`s cannot be empty!!!'
    ha=hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb=hashlib.sha1(b .encode('utf-8')).hexdigest()
    if verbose:
        print(ha, hb, sep='\n')
    return ha == hb


s_1 = input('Enter first string: ')
s_2 = input('Enter second string: ')
print('String`s is equvile' if is_eq_str(s_1, s_2, True) else 'Different string`s')
