# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям
# (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

n = int(input('Сколько друзей встретилось? Введите число: '))
graph = []
count = 0
for i in range(n):
    frend = []
    for j in range(n):
        if i == j:
            frend.append(0)
        else:
            frend.append(1)
            count += 1
    graph.append(frend)
print('Матрица смежности: ')
print(*graph, sep='\n')
print('*' * 50)
print(f'Общее количество рукопожатий для {n} друзей: {count//2}')
