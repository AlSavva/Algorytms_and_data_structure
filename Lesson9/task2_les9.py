# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter, namedtuple
import heapq

Node = namedtuple('Node', ['left', 'right'])
Leaf = namedtuple('Leaf', ['symbol'])


def huffman_code(string):
    fdeq = []
    for letter, freq in Counter(string).items():
        fdeq.append((freq, len(fdeq), Leaf(letter)))
    heapq.heapify(fdeq)
    count = len(fdeq)
    while len(fdeq) > 1:
        freq1, _count1, left = heapq.heappop(fdeq)
        freq2, _count2, right = heapq.heappop(fdeq)
        heapq.heappush(fdeq, (freq1 + freq2, count, Node(left, right)))
        count += 1
        print(fdeq)
    [(_freq, _count, root)]=fdeq
    code = {}
    path = ''

    def bts(fdeq):
        global path
        if isinstance(fdeq, Leaf):
            code[fdeq.symbol] = path
        else:
            if isinstance(fdeq.left, Node):
                path += '0'
                bts(fdeq.left)
            if isinstance(fdeq.right, Node):
                path += '1'
                bts(fdeq.right)
        print(code)
    return code













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
print(huffman_code(k))