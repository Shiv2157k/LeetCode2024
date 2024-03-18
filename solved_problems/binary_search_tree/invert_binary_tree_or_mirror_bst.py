from collections import deque
from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def invert_v1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Iterative
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return root

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

    def invert_v0(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        if not root:
            return root

        left = self.invert_v0(root.left)
        right = self.invert_v0(root.right)

        root.right = left
        root.left = right

        return root
