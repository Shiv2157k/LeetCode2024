from typing import Optional, List
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def level_order_bottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: BFS Deque
        :param root:
        :return:
        """

        if not root:
            return []

        levels = deque()
        queue = deque([root])

        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node)

                for child_node in (node.left, node.right):
                    if child_node:
                        queue.append(child_node)
            levels.appendleft(level)
        return list(levels)
