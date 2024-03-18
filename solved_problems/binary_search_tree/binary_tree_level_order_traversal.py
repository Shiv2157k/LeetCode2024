from collections import deque
from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:

    def level_order_traversal_v1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Iteration
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        levels = []

        if not root:
            return levels

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels

    def level_order_traversal_v0(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Recursion
        T: O(N)
        S: O(H)
        :param root:
        :return:
        """
        levels = []
        if not root:
            return levels

        def traverse_level(node: Optional[TreeNode], level: int):
            if level == len(levels):
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                traverse_level(node.left, level + 1)
            if node.right:
                traverse_level(node.right, level + 1)

        traverse_level(root, 0)
        return levels
