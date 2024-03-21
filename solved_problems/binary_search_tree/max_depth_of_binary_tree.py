from typing import Optional
from collections import deque


class TreeNode:

    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def max_depth_v0(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        else:
            left_height = self.max_depth_v0(root.left)
            right_height = self.max_depth_v0(root.right)
            return 1 + max(left_height, right_height)

    def max_depth_v1(self, root: Optional[TreeNode]) -> int:
        """
        Iterative
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return 0
        queue = deque()
        queue.append(root)

        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth