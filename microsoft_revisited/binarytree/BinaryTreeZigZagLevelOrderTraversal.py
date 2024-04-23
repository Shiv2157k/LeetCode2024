from typing import Optional, List
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def zigZagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: BFS or Queue
        :param root:
        :return:
        """
        if not root:
            return []

        queue = deque([(root, 0)])
        levels = []
        while queue:
            levelOrder = deque()
            size = len(queue)
            for _ in range(size):
                node, level = queue.popleft()
                if level % 2 == 0:
                    levelOrder.append(node.val)
                else:
                    levelOrder.appendleft(node.val)
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

            levels.append(levelOrder)
        return levels
