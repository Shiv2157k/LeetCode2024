from typing import Optional
from math import inf


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def isValidBSTV3(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: InOrder Iterative
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        stack = []
        prev = -inf

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

    def isValidBSTV2(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Inorder Recursive
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def inOrder(root):
            nonlocal prev
            if not root:
                return True

            if not inOrder(root.left):
                return False

            if root.val <= prev:
                return False
            prev = root.val
            return inOrder(root.right)

        prev = -inf
        return inOrder(root)

    def isValidBSTV1(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Iterative Stack
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

            val = node.val
            if val <= low or val >= high:
                return False
            stack.append((node.left, node.val, high))
            stack.append((node.right, low, node.val))
        return True

    def isValidBSTV0(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Recursion Stack
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def validate(node: Optional[TreeNode], low: int = -inf, high: int = inf):

            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (validate(node.left, low, node.val) and validate(node.right, node.val, high))

        return validate(root)
