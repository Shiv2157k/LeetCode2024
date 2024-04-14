from math import inf
from typing import Optional


class TreeNode:

    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def isValidBSTV0(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Recursive
        :param root:
        :return:
        """

        def validate(node: Optional[TreeNode], low: int = -inf, high: int = inf):

            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root)

    def isValidBSTV01(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Stack
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return True

        stack = [(root, -inf, inf)]

        while stack:

            node, low, high = stack.pop()

            if not node:
                continue

            if node.val <= low or node.val >= high:
                return False

            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))
        return True

    def isValidBSTV1(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Iterative Inorder Traversal
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        stack = []
        prev = -inf

        while root or stack:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if prev <= root.val:
                return False
            prev = root.val
            root = root.right
        return True
