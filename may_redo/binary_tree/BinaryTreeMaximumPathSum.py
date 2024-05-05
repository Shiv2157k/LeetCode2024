from typing import Optional
from math import inf


class TreeNode:

    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Post order dfs
        T: O(N)
        S: O(N)
        :param root: 
        :return:
        """

        def gain_from_subtrees(node: Optional[TreeNode]) -> int:
            nonlocal max_gain

            if not node:
                return 0

            left_gain = max(gain_from_subtrees(node.left), 0)
            right_gain = max(gain_from_subtrees(node.right), 0)
            max_gain = max(max_gain, left_gain + right_gain + node.val)
            return max(left_gain + node.val, right_gain + node.val)

        max_gain = -inf
        gain_from_subtrees(root)
        return max_gain
