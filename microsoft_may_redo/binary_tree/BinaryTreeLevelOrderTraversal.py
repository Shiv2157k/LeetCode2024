from typing import Optional, List
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def level_order_traversal_v1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: Queue BFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return []

        queue = deque([root])
        levels = []

        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels

    def level_order_traversal_v0(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        levels = []

        def helper(node: Optional[TreeNode], level) -> None:

            if not node:
                return

            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)
            for child_node in (node.left, node.right):
                if child_node:
                    helper(child_node, level + 1)

        helper(root, 0)
        return levels
