from collections import deque
from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def is_same_tree_v0(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param p:
        :param q:
        :return:
        """

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.is_same_tree_v0(p.right, q.right) and self.is_same_tree_v0(p.left, q.left)

    def is_same_tree_v1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach: Iteration
        T: O(N)
        S: O(N)
        :param p:
        :param q:
        :return:
        """

        def is_same(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        queue = deque()
        queue.append((p, q))

        while queue:
            p, q = queue.popleft()
            if not is_same(p, q):
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True