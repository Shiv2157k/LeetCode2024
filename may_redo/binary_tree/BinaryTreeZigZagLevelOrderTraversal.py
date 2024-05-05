from collections import deque
from typing import Optional, List


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def zigzag_level_order_v1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: BFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        queue = deque([(root, 0)])
        levels = []

        while queue:
            level_order = deque()
            size = len(queue)
            for _ in range(size):

                node, level = queue.popleft()

                if level % 2 == 0:
                    level_order.append(node.val)
                else:
                    level_order.appendleft(node.val)

                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
                    
            levels.append(list(level_order))
        return levels

    def zigzag_level_order_v0(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: DFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        def traverse(node: Optional[TreeNode], level: int):

            if len(level_order) == level:
                level_order.append(deque())
            if level % 2 == 0:
                level_order[level].append(node.val)
            else:
                level_order[level].appendleft(node.val)

            for child_node in (node.left, node.right):
                if child_node:
                    traverse(child_node, level + 1)

        level_order = []
        traverse(root, 0)
        return level_order

