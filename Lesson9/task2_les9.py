# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter, namedtuple

Leaf = namedtuple('Leaf', ['symb'])
"""
defining the Leaf class-to denote the leaves of a binary tree.
"""


def huffman_coding(string):
    """
    coding function for the Huffman algorithm
    """
    def bts(lst, path=None, code=None):
        """
        recursive path search in a binary tree
        """
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

    deq = []
    for symbol, frequency, in Counter(string).items():
        deq.append([frequency, Leaf(symbol)])
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
