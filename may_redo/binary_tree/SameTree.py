from typing import Optional
from collections import deque


class TreeNode:

    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def is_same_tree_v1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach: BFS Queue
        T: O(N)
        S: O(N)
        :param p:
        :param q:
        :return:
        """

        def is_same(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:

            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return True

        queue = deque([(p, q)])

        while queue:
            p, q = queue.popleft()

            if not is_same(p, q):
                return False

            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True

    def is_same_tree_v0(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Approach: DFS Recursion
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
        return self.is_same_tree_v0(p.left, q.left) and self.is_same_tree_v0(p.right, q.right)
