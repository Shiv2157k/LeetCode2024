from typing import Optional
from math import inf


class TreeNode:

    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def binary_tree_max_path_sum(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Recursion
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def gain_from_subtrees(node: Optional[TreeNode]) -> int:
            nonlocal max_gain

            if not root:
                return 0

            left_gain = max(0, gain_from_subtrees(node.left))
            right_gain = max(0, gain_from_subtrees(node.right))

            max_gain = max(max_gain, left_gain + right_gain + node.val)

            return max(left_gain + node.val, right_gain + node.val)

        max_gain = -inf
        gain_from_subtrees(root)
        return max_gain
