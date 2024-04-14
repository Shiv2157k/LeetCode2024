from typing import Optional


class Node:

    def __init__(self, val: int=-1, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class BinaryTree:


    def flipBinaryTree(self, root: Optional[Node], leaf: Optional[Node]):
        """
        Approach: Iteration as per rules
        T: O(N)
        S: O(N)
        :param root:
        :param leaf:
        :return:
        """
        node, prev = leaf, None

        while node != root:

            # case 1: if left tree exists nodes right will be left
            if node.left:
                node.right = node.left

            # case 2: nodes parent will be its left child and nodes parent will be None
            node.left, node.parent = node.parent, prev
            # traverse to next level
            node, prev = node.left, node

            # to handle cycles
            if node.left == prev:
                node.left = None
            else:
                node.right = None
        root.parent = prev
        return leaf
