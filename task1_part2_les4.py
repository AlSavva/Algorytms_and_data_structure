import functools

def multiple_num(n):
    """Функция выводит количество чисел из диапазона от 2 до n,
    кратных числам от 2 до 9"""
    div2 = div3 = div5 = div7 = 0
    for num in range(2, n + 1):
        if num % 2 == 0:
            div2 += 1
        if num % 3 == 0:
            div3 += 1
        if num % 5 == 0:
            div5 += 1
        if num % 7 == 0:
            div7 += 1
    return (div2, div3, div2 // 2, div5, div3 // 2, div7, div2 // 4, div3 // 3)

# "task1_part2_les4.multiple_num(99)"
# 100 loops, best of 5: 20.6 usec per loop

# "task1_part2_les4.multiple_num(999)"
# 100 loops, best of 5: 213 usec per loop

# "task1_part2_les4.multiple_num(9999)"
# 100 loops, best of 5: 2.17 msec per loop

# "task1_part2_les4.multiple_num(99999)"
# 100 loops, best of 5: 22 msec per loop


@functools.lru_cache()
def multiple_num1(n):
    """Функция выводит количество чисел из диапазона от 2 до n,
    кратных числам от 2 до 9"""
    div2 = div3 = div5 = div7 = 0
    for num in range(2, n + 1):
        if num % 2 == 0:
            div2 += 1
        if num % 3 == 0:
            div3 += 1
        if num % 5 == 0:
            div5 += 1
        if num % 7 == 0:
            div7 += 1
    return [div2, div3, div2 // 2, div5, div3 // 2, div7, div2 // 4, div3 // 3]

# "task1_part2_les4.multiple_num1(99)"
# 1000 loops, best of 5: 84.8 nsec per loop

# "task1_part2_les4.multiple_num1(999)"
# 1000 loops, best of 5: 81.4 nsec per loop

# "task1_part2_les4.multiple_num1(999999)"
# 1000 loops, best of 5: 81.7 nsec per loop

def multiple_num2(n):
    a = [0] * 8
    for num in range(2, n + 1):
        for i in range(2, 10):
            if num % i == 0:
                a[i - 2] += 1
    return [a[num] for num in range(len(a))]

# "task1_part2_les4.multiple_num2(99)"
# 100 loops, best of 5: 74.7 usec per loop

# "task1_part2_les4.multiple_num2(999)"
# 100 loops, best of 5: 754 usec per loop

# "task1_part2_les4.multiple_num2(9999)"
# 100 loops, best of 5: 7.9 msec per loop

# "task1_part2_les4.multiple_num2(99999)"
# 100 loops, best of 5: 77.8 msec per loop

@functools.lru_cache()
def multiple_num3(n):
    a = [0] * 8
    for num in range(2, n + 1):
        for i in range(2, 10):
            if num % i == 0:
                a[i - 2] += 1
    return [a[num] for num in range(len(a))]

# "task1_part2_les4.multiple_num3(99)"
# 100 loops, best of 5: 85 nsec per loop

# "task1_part2_les4.multiple_num3(999)"
# 100 loops, best of 5: 91 nsec per loop

# "task1_part2_les4.multiple_num3(9999)"
# 100 loops, best of 5: 88 nsec per loop

# "task1_part2_les4.multiple_num3(99999)"
# 100 loops, best of 5: 88 nsec per loop

# Вывод при одинаковой вычислительной сложности O(n)
# функция multiple_num работает примерно в 4 раза быстее чем multiple_num2,
# однако применение @functools.lru_cache() упрощает сложность данных алгоритмов
# до О(1), и нивелирует разницу в скорости.