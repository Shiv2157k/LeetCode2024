from typing import Optional, List
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def level_order_v1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: BFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []
        queue = deque([root])
        level_order = []

        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()

                if node:
                    level.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            level_order.append(level)
        return level_order

    def level_order_v0(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        def traversal(node: Optional[TreeNode], level: int):

            if node:
                if len(level_order) == level:
                    level_order.append([])

                level_order[level].append(node.val)

                for child_node in (node.left, node.right):
                    if child_node:
                        traversal(child_node, level + 1)

        level_order = []
        traversal(root, 0)
        return level_order
