from typing import Optional
from collections import deque


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def max_depth_vo(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if root is None:
            return 0
        else:
            left_height = self.max_depth_vo(root.left)
            right_height = self.max_depth_vo(root.right)
            return max(left_height, right_height) + 1

    def max_depth_v1(self, root: Optional[TreeNode]) -> int:
        """
        Approach: BFS Iterative
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return 0

        queue = deque([root])
        level = 0

        while queue:
            level += 1
            size = len(queue)
            for _ in range(size):
                root = queue.popleft()

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return level
