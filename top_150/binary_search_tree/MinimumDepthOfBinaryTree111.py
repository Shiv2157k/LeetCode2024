from typing import Optional
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def minimumDepthOfTreeV0(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def dfs(root: Optional[TreeNode]) -> int:

            if not root:
                return 0

            if not root.left:
                return 1 + dfs(root.right)
            if not root.right:
                return 1 + dfs(root.left)
            return 1 + min(dfs(root.left), dfs(root.right))

        return dfs(root)

    def minimumDepthOfTreeV1(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Queue (BFS)
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            curr, depth = queue.popleft()
            if curr.left is None and curr.right is None:
                return depth
            if curr.left:
                queue.append((curr.left, depth + 1))
            if curr.right:
                queue.append((curr.right, depth + 1))
