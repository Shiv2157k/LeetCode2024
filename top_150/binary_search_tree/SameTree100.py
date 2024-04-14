from collections import deque
from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def isSameTreeV1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach: BFS
        T: O(H)
        S: O(H)
        :param p:
        :param q:
        :return:
        """

        queue = deque()
        queue.append((p, q),)

        def isValid(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        while queue:
            p, q = queue.popleft()

            if not isValid(p, q):
                return False

            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True

    def isSameTreeV0(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach: Recursion
        T: O(H)
        S: O(H)
        :param p:
        :param q:
        :return:
        """
        if not p or not q:
            return False
        if not p and not q:
            return True

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
