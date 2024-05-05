from typing import Optional



class TreeNode:

    def __init__(self, val: int=-1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:


    def get_diameter(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Recursion
        T: O(N)
        S: O(H)
        :param root:
        :return:
        """

        diameter = 0

        def longest_path(node):

            if not node:
                return 0

            nonlocal diameter

            left_path: int = longest_path(node.left)
            right_path: int = longest_path(node.right)

            diameter = max(diameter, left_path + right_path)
            return max(left_path, right_path) + 1
        longest_path(root)
        return diameter