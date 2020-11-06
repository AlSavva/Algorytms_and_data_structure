from collections import Counter, namedtuple
import heapq
Leaf=namedtuple('Leaf', ['symb', ])
Node=namedtuple('Node',['left', 'right'])


s = 'beep boop beer!'
con= Counter(s)
print(con)
deq = []
for key, values in con.items():
    deq.append((int(values), len(deq), Leaf(key)))
heapq.heapify(deq)
# deq=sorted(deq)
# deq = [(1, Leaf(symb='r')), (1, Leaf(symb='!')), (2, Leaf(symb='p')), (2, Leaf(symb='o')), (2, Leaf(symb=' ')), (3, Leaf(symb='b')), (4, Leaf(symb='e'))]
print(deq)
count = len(deq)
while len(deq)>1:
    # freq1, node1 = deq.pop(0)
    freq1, _count1, node1 = heapq.heappop(deq)
    # freq2, node2 = deq.pop(0)
    freq2, _count2, node2 = heapq.heappop(deq)
    # deq.append((freq1 + freq2, (node1, node2)))
    heapq.heappush(deq, (freq1 + freq2, count, (node1, node2)))
    count += 1

    # for i in range(len(deq)-1):
    #     if deq[i][0]>=deq[-1][0]:
    #         a=deq.pop()
    #         deq.insert(i, a)
    #         break
root = deq[0][2]
print(deq)
print(root)


def bts(lst, path=None, code={}):
    if path is None:
        path=''
    if isinstance(lst, Leaf):
        if lst.symb not in code:
            code[lst.symb]=[]
        code[lst.symb].append(path)

    else:
        for i in range(2):
            path=path+str(i)
            bts(lst[i],path,code)


        return code

print(bts(root))
# {'b': ['00'], 'o': ['0010'], ' ': ['00101'], 'r': ['01000'], '!': ['010001'], 'p': ['01001'], 'e': ['0101']}
# {'b': ['00'], 'o': ['0010'], 'p': ['00101'], '!': ['01000'], 'r': ['010001'], ' ': ['01001'], 'e': ['0101']}
# {'p': ['00'], 'o': ['0010'], 'b': ['00101'], 'r': ['0100'], '!': ['010010'], ' ': ['0100101'], 'e': ['0101']}
# {'b': ['00'], 'e': ['001'], 'p': ['0100'], ' ': ['01001'], 'o': ['01010'], 'r': ['0101010'], '!': ['01010101']}