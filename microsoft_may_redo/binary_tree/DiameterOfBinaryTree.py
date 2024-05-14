from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def diameter_of_bst(self, root: Optional[TreeNode]) -> int:
        """
        Approach: DFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        diameter = 0

        def longest_path(node: Optional[TreeNode]):
            nonlocal diameter
            if not node:
                return 0

            left = longest_path(node.left)
            right = longest_path(node.right)

            diameter = max(diameter, left + right)
            return max(left, right) + 1

        longest_path(root)
        return diameter
