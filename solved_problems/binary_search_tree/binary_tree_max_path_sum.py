from typing import Optional


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Pre-order Traversal
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """
        max_gain = int("-inf")

        def gain_from_tree(node: Optional[TreeNode]) -> int:
            nonlocal max_gain
            if not node:
                return 0

            left_gain = max(gain_from_tree(node.left), 0)
            right_gain = max(gain_from_tree(node.right), 0)
            max_gain = max(max_gain, left_gain + right_gain + node.val)
            return max(left_gain + node.val, right_gain + node.val)

        gain_from_tree(root)
        return max_gain
