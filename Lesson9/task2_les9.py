# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter, namedtuple

Leaf = namedtuple('Leaf', ['symb'])


def huffman_coding(string):
    def bts(lst, path=None, code=None):
        if path is None:
            path = ''
        if code is None:
            code = {}
        if isinstance(lst, Leaf):
            if lst.symb not in code:
                code[lst.symb] = ''
            code[lst.symb] += path
        else:
            for i in range(2):
                bts(lst[i], path + str(i), code)
        return code

    con = Counter(string)
    deq = []
    for key, values in con.items():
        deq.append([int(values), Leaf(key)])
    deq = sorted(deq)
    while len(deq) > 1:
        freq1, node1 = deq.pop(0)
        freq2, node2 = deq.pop(0)
        deq.append([freq1 + freq2, [node1, node2]])
        for i in range(len(deq) - 1):
            if deq[i][0] >= deq[-1][0]:
                a = deq.pop()
                deq.insert(i, a)
                break
    print(f'Original string: {string}')
    print(f'Code key`s: {bts(deq[0][1])}')
    return f'Encoded string: {" ".join([bts(deq[0][1])[i] for i in string])}'


s = 'beep boop beer!'
print(huffman_coding(s))













s = 'beep boop beer!'
a=Counter(s)
print(a)
m = huffman_code(s)
print(m)
# print(n)
# print(bts(n))
# print(bts(m))

k=Node(left=Node(left=Leaf(symbol='b'),right=Node(left=Leaf(symbol='o'), right=Leaf(symbol=' '))),
     right=Node(left=Node(left=Node(left=Leaf(symbol='r'),right=Leaf(symbol='!')), right=Leaf(symbol='p')),
     right=Leaf(symbol='e')))
print(type(k))
print(bts(k))