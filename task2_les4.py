# Написать два алгоритма нахождения i-го по счёту простого числа. Функция
# нахождения простого числа должна принимать на вход натуральное и возвращать
# соответствующее простое число. Проанализировать скорость и сложность
# алгоритмов.
import cProfile


def erat(n):
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1129: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8
               }  # и-функция - количество простых чисел в заданном интервале
    for key in pi_func.keys():
        if n <= key:
            size = pi_func[key]
            break
    sieve = [i for i in range(size)]
    sieve[1] = 0
    for i in range(2, size):
        if sieve[i] != 0:
            j = i ** 2
            while j < size:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res[n - 1]


# "task2_les4.erat(100)"
# 100 loops, best of 5: 270 usec per loop

# "task2_les4.erat(1000)"
# 100 loops, best of 5: 3.04 msec per loop

# "task2_les4.erat(10000)"
# 1000 loops, best of 5: 386 msec per loop

# Модернизируем Решето:
def erat1(n):
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1129: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8
               }  # и-функция - количество простых чисел в заданном интервале
    for key in pi_func.keys():
        if n <= key:
            size = pi_func[key]
            break
    sieve = [True for i in range(size)]
    sieve[:2] = [False, False]
    count = 0
    for i in range(2, size):
        if sieve[i]:
            count += 1
            if count == n:
                return i
            for j in range(i ** 2, size, i):
                sieve[j] = False

# "task2_les4.erat1(100)"
# 100 loops, best of 5: 152 usec per loop

# "task2_les4.erat1(1000)"
# 100 loops, best of 5: 1.68 msec per loop

# "task2_les4.erat1(10000)"
# 100 loops, best of 5: 163 msec per loop

def my_simple(n):
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1129: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8
               }
    for key in pi_func.keys():
        if n <= key:
            size = pi_func[key]
            break
    lst = []
    for i in range(2, size + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[n - 1]


# "task2_les4.my_simple(100)"
# 1000 loops, best of 5: 4.3 msec per loop

# "task2_les4.my_simple(1000)"
# 1000 loops, best of 5: 406 msec per loop


# Как видно из анализа сложность Алгоритма Решето Эратосфена O(n)
# А сложность алгоритма с циклами О(n**2) из за 2-х вложенных циклов

def my_simple1(n):
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1129: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8
               }
    for key in pi_func.keys():
        if n <= key:
            size = pi_func[key]
            break
    lst = [2]
    for i in range(3, size + 1, 2):
        if i > 10 and i % 10 == 5:
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[n - 1]

# "task2_les4.my_simple1(100)"
# 100 loops, best of 5: 295 usec per loop

# "task2_les4.my_simple1(1000)"
# 100 loops, best of 5: 5.35 msec per loop

# "task2_les4.my_simple1(10000)"
# 100 loops, best of 5: 1.82 sec per loop

# "task2_les4.my_simple1(1000)"
# 100 loops, best of 5: 293 usec per loop

# Алгоритм с дывумя циклами можно модифицировать, приблизив его к линейной
# зависимости О(n) путем вложения второго цикла в условный оператор. Так же
# возможно модифицировать решето. Которое является лучшим алгоритмом из
# представленных.

# cProfile.run('erat(1000)')
# 7 function calls in 0.003 seconds

# cProfile.run('erat1(1000)')
# 6 function calls in 0.002 seconds

# cProfile.run('my_simple(1000)')
# 1234 function calls in 0.359 seconds
# 1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('my_simple1(1000)')
# 1233 function calls in 0.005 seconds
# 1228    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
