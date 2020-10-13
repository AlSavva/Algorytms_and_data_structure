# Написать два алгоритма нахождения i-го по счёту простого числа. Функция
# нахождения простого числа должна принимать на вход натуральное и возвращать
# соответствующее простое число. Проанализировать скорость и сложность
# алгоритмов.


def erat(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res


# "task2_les4.erat(100)"
# 1000 loops, best of 5: 22.4 usec per loop

# "task2_les4.erat(200)"
# 1000 loops, best of 5: 46.4 usec per loop

# "task2_les4.erat(400)"
# 1000 loops, best of 5: 102 usec per loop

# "task2_les4.erat(1000)"
# 1000 loops, best of 5: 272 usec per loop


def my_simple(n):
    lst = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


# "task2_les4.my_simple(100)"
# 1000 loops, best of 5: 72.4 usec per loop

# "task2_les4.my_simple(200)"
# 1000 loops, best of 5: 246 usec per loop

# "task2_les4.my_simple(400)"
# 1000 loops, best of 5: 768 usec per loop

# "task2_les4.my_simple(1000)"
# 1000 loops, best of 5: 4.21 msec per loop

# Как видно из анализа сложность Алгоритма Решето Эратосфена O(n*log(logn))
# А сложность алгоритма с циклами О(n**2) из за 2-х вложенных циклов

def my_simple1(n):
    lst = [2]
    for i in range(3, n + 1, 2):
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
    return lst

# "task2_les4.my_simple1(100)"
# 100 loops, best of 5: 19.4 usec per loop

# "task2_les4.my_simple1(200)"
# 100 loops, best of 5: 43.8 usec per loop

# "task2_les4.my_simple1(400)"
# 100 loops, best of 5: 97.4 usec per loop

# "task2_les4.my_simple1(1000)"
# 100 loops, best of 5: 293 usec per loop

# Алгоритм с дывумя циклами можно модифицировать, приблизив его к линейной
# зависимости О(n) путем вложения второго цикла в условный оператор.