from typing import Optional, List
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def zig_zag_level_order_traversal_v1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: BFS Traversal using Queue
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
            level = deque()
            size = len(queue)
            for _ in range(size):

                node, curr_level = queue.popleft()
                if curr_level % 2 == 1:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)
                if node.left:
                    queue.append((node.left, curr_level + 1))
                if node.right:
                    queue.append((node.right, curr_level + 1))
            levels.append(list(level))
        return levels

    def zig_zag_level_order_traversal_v0(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: Recursion
        T: O(N)
        S: O(H)
        :param root:
        :return:
        """

        def dfs(node, level: int) -> None:
            if not node:
                return

            if len(levels) == level:
                levels.append(deque())

            if level % 2 == 1:
                levels[level].appendleft(node.val)
            else:
                levels[level].append(node.val)

            for child_node in (node.left, node.right):
                if child_node:
                    dfs(child_node, level + 1)

        levels = []
        dfs(root, 0)
        return levels
