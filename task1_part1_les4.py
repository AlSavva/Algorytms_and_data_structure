# Проанализировать скорость и сложность одного любого алгоритма из
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не
# забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.
import timeit
import cProfile
import functools

def str_numreverse(n):
    """Функция выводит введёное число в обратном порядке(рекурсия)"""
    if n // 10 < 1:
        return str(n)
    return str(n % 10) + str_numreverse(n // 10)

# "task1_part1_les4.str_numreverse(10**10)"
# 1000 loops, best of 5: 3.83 usec per loop     11**10

# "task1_part1_les4.str_numreverse(10**100)"
# 1000 loops, best of 5: 42.7 usec per loop     11**100

# "task1_part1_les4.str_numreverse(10**500)"
# 1000 loops, best of 5: 340 usec per loop      11**500

# "task1_part1_les4.str_numreverse(10**800)"
# 1000 loops, best of 5: 762 usec per loop      11**800

# "task1_part1_les4.str_numreverse(10**1000)"
# RecursionError: maximum recursion depth       11**1000




def str_numreverse1(n):
    """Функция выводит введёное число в обратном порядке(не рекурсия)"""
    m = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        m = m * 10
        m = m + digit
    return m

# "task1_part1_les4.str_numreverse(11**10)"
# 1000 loops, best of 5: 1.8 usec per loop     11**10

# "task1_part1_les4.str_numreverse(11**100)"
# 1000 loops, best of 5: 24.6 usec per loop     11**100

# "task1_part1_les4.str_numreverse1(11**500)"
# 1000 loops, best of 5: 215 usec per loop      11**500

# "task1_part1_les4.str_numreverse1(11**800)"
# 1000 loops, best of 5: 451 usec per loop      11**800

# "task1_part1_les4.str_numreverse1(11**1000)"
# 1000 loops, best of 5: 655 usec per loop      11**1000

# "task1_part1_les4.str_numreverse1(11**10000)"
# 1000 loops, best of 5: 49.1 msec per loop     11**10000


@functools.lru_cache()
def str_numreverse2(n):
    """Функция выводит введёное число в обратном порядке(рекурсия)"""
    if n // 10 < 1:
        return str(n)
    return str(n % 10) + str_numreverse(n // 10)

# "task1_part1_les4.str_numreverse2(11**10)"
# 1000 loops, best of 5: 86 nsec per loop       11**10

# "task1_part1_les4.str_numreverse2(11**100)"
# 1000 loops, best of 5: 521 nsec per loop      11**100

# "task1_part1_les4.str_numreverse2(11**800)"
# 1000 loops, best of 5: 2.73 usec per loop     11**800

# "task1_part1_les4.str_numreverse(10**1000)"
# RecursionError: maximum recursion depth       11**1000

# Вывод - алгоритм с циклом  не имеет ограничений по стеку, однако если нужно
# "перевернуть" меньшее чем 10**1000 быстрее сего будет работать рекурсия с
# декоратором @functools.lru_cache()