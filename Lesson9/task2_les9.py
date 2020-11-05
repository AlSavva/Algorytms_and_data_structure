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
    root = fdeq[0][2]
    return root


code = {}
path = ''


def bts(root):
    global path
    if isinstance(root.left, Leaf):
        path += '0'
        code[root.left.symbol] = path + '0'

    else:
        # path += '0'
        bts(root.left)
    if isinstance(root.right, Leaf):
        path += '1'
        code[root.right.symbol] = path + '1'

    else:
        # path += '1'
        bts(root.right)
    # if not isinstance(root.left, Leaf):
    #     bts(root.left)
    # if not isinstance(root.right, Leaf):
    #     bts(root.right)
    return code


# print(fdeq[0][1])
# return fdeq

s = 'beep boop beer!'
m = huffman_code(s)
n = Node(left=Node(left=Leaf(symbol='b'), right=Node(left=Leaf(symbol='o'), right=Leaf(symbol=' '))),
         right=Node(left=Node(left=Node(left=Leaf(symbol='r'), right=Leaf(symbol='!')), right=Leaf(symbol='p')), right=Leaf(symbol='e')))
print(m)
print(n)
print(bts(n))
print(bts(m))