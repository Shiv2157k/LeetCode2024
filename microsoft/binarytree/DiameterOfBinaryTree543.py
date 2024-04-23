from typing import Optional


class TreeNode:

    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        diameter = 0

        def longest(node: Optional[TreeNode]) -> int:
            # base case
            if not node:
                return 0
            # handle two cases
            # case 1: left -> node -> right
            # case 2: left -> node -> upwards
            nonlocal diameter

            leftPath = longest(node.left)
            rightPath = longest(node.right)

            diameter = max(diameter, leftPath + rightPath)

            return max(leftPath, rightPath) + 1

        longest(root)
        return diameter
