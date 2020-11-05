# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter, namedtuple
import heapq

Node = namedtuple('Node', ['left', 'right'])
Leaf = namedtuple('Leaf', ['symbol'])


def huffman_code(string):
    fdeq = [(freq, symbol) for symbol, freq in Counter(string).items()]
    heapq.heapify(fdeq)
    while len(fdeq) > 1:
        freq1, left = heapq.heappop(fdeq)
        freq2, right = heapq.heappop(fdeq)
        heapq.heappush(fdeq, (freq1 + freq2, Node(left, right)))
    print(fdeq)


# root = Node(left=Node(left='r', right='e'),
#             right=Node(left=Node(left='p', right=Node(left='!', right=' ')),
#                        right=Node(left='o', right='b')))
# print(f"!!!!!!!!!!!!!!!!!!!{root}")
#
# code = {}
# path=''
# def bts(root):
#     global path
#     if isinstance(root.left, str):
#         path+='0'
#         code[root.left] = path
#     if isinstance(root.right, str):
#         path+='1'
#         code[root.right] = path
#     if not isinstance(root.left, str):
#         bts(root.left)
#     if not isinstance(root.right, str):
#         bts(root.right)
#     print(code)


# print(fdeq[0][1])
# return fdeq

string = 'beep boop beer!'
huffman_code(string)
bts(root)
