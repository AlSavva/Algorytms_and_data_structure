# по умолчанию в Python нет деревьев
from binarytree import tree, bst, Node, build


# дерево можно создать написанием класса
class MyNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.rigt = right


# можно воспользоваться библиотекой binary tree
# с помощью функции tree:
print('создано с помощью функции "tree"', '*' * 33, sep='\n')

a = tree(height=4, is_perfect=False)
# height=4 задаем высоту дерева, is_perfect=False указываем - что оно не
# расширенное
print(a)
# с помощью функции bst строятся бинарные поисковые деревья:
print('создано с помощью функции "bst"', '*' * 33, sep='\n')
b = bst(height=4, is_perfect=True)
print(b)
# с помощью создания экземпляров класса Node:
print('создано с помощью класса "Node"', '*' * 33, sep='\n')
c = Node(15)  # задаем корень дерева
c.left = Node(7)
c.right = Node(23)
c.left.left = Node(3)
c.left.right = Node(11)
c.right.left = Node(19)
c.right.right = Node(27)
c.left.left.left = Node(1)
c.left.left.right = Node(5)
c.left.right.left = Node(9)
c.left.right.right = Node(13)
c.right.left.left = Node(17)
c.right.left.right = Node(21)
c.right.right.left = Node(25)
c.right.right.right = Node(29)
print(c)
# с помощью функции build:
print('создано с помощью функции "build"', '*' * 33, sep='\n')
print("идеальное дерево")
d = build([15, 7, 23, 3, 11, 19, 17, 1, 5, 9, 13, 17, 21, 25, 29])
print(d)
print('создано с помощью функции "build"', '*' * 33, sep='\n')
print("неполное дерево")
d = build([15, 7, 23, 3, 11, 19, 17, None, 5, None, 13, 17, None, 25, 29])
print(d)
