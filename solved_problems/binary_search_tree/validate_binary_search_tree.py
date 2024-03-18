from math import inf
from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.prev = -inf

    def validate_v3(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Iterative Inorder
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        stack, prev = [], -inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True

    def validate_v2(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Recursive Inorder
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        self.prev = -inf

        def in_order(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            if not in_order(node.left):
                return False
            if node.val <= self.prev:
                return False

            self.prev = node.val
            in_order(node.right)
        in_order(root)

    def validate_v1(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Iterative
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return True
        stack = [(root, -inf, inf)]

        while stack:
            root, low, high = stack.pop()

            if root.val <= low or root.val >= high:
                return False
            if root.right:
                stack.append((root.right, root.val, high))
            if root.left:
                stack.append((root.left, low, root.val))
        return True

    def validate_v0(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def is_valid(node: Optional[TreeNode], low: int = -inf, high: int = inf) -> bool:
            # leaf nodes are valid base case
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return is_valid(node.left, low, node.val) and is_valid(node.right, node.val, high)

        return is_valid(root)
