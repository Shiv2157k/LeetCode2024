from typing import Optional
from math import inf


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def validate_tree_v3(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Iterative inorder
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        if not root:
            return True

        stack = []
        prev = -inf

        while stack or root:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if prev >= root.val:
                return False
            prev = root.val
            root = root.right
        return True

    def validate_tree_v2(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Recursion Inorder
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        prev = -inf

        def inorder(root):
            nonlocal prev
            if not root:
                return True

            if not inorder(root.left):
                return False
            if root.left >= prev:
                return False
            prev = root.val
            return inorder(root.right)

        return inorder(root)

    def validate_tree_v1(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Iterative Stack
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
            curr_val = node.val
            if curr_val <= low or curr_val >= high:
                return False
            stack.append((node.right, curr_val, high))
            stack.append((node.left, low, curr_val))
        return True
    
    def validate_tree_v0(self, root: Optional[TreeNode]) -> bool:

        def validate(node: Optional[TreeNode], low=-inf, high=inf):

            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root)
