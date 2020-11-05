# Алгоритм бинарного поиска по дереву (bunary tree searc - bts:

from binarytree import bst


def bts(bin_search_tree, number, path=''):
    if bin_search_tree.value == number:
        return f'Find {number}.\nPath:\nRoot{path}'
    if number <bin_search_tree.value and bin_search_tree.left!=None:
        return bts(bin_search_tree.left, number, path=f'{path}\nStep left')
    if number >bin_search_tree.value and bin_search_tree.right!=None:
        return bts(bin_search_tree.right, number, path=f'{path}\nStep right')
    return f'{number} out of tree'

bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input('enter target number: '))
print(bts(bt, num))
