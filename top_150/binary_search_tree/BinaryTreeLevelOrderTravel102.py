from collections import deque
from typing import List, Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def levelOrderV0(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: DFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []
        levels = []

        def dfs(node: Optional[TreeNode], level: int) -> None:

            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)
        return levels

    def levelOrderV1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: BFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return []

        queue = deque()
        queue.append(root)
        levels = []

        while queue:

            size = len(queue)
            level = []
            for _ in range(size):

                root = queue.popleft()

                level.append(root.val)

                if root:
                    queue.append(root.left)
                    queue.append(root.right)
            levels.append(level)
        return levels
