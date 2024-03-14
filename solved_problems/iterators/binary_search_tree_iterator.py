from typing import Optional


class BSTNode:

    def __init__(self, value: int = -1):
        self.val = value
        self.left = None
        self.right = None


class BinarySearchIteratorV1:

    def __init__(self, root: Optional[BSTNode]):
        self._stack = []
        self._left_inorder(root)

    def _left_inorder(self, node: Optional[BSTNode]):
        while node:
            self._stack.append(node)
            node = node.left

    def next(self):
        """ O(1)"""
        if self._stack:
            top_most_node = self._stack.pop()
            if top_most_node.right:
                self._left_inorder(top_most_node.right)
            return top_most_node.val

    def hasNext(self):
        """ O(1)"""
        return len(self._stack) > 0


class BinarySearchIteratorV0:

    def __init__(self, root: Optional[BSTNode]):
        self._sorted_nodes = []
        self._pointer = -1
        self._in_order(root)

    def _in_order(self, node: Optional[BSTNode]):
        while node:
            self._in_order(node.left)
            self._sorted_nodes.append(node.val)
            self._in_order(node.right)

    def next(self):
        self._pointer += 1
        return self._sorted_nodes[self._pointer]

    def hasNext(self):
        return self._pointer + 1 < len(self._sorted_nodes)