from typing import Optional
from math import inf


class TreeNode:

    def __init__(self, val: int = -1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Approach: DFS
        T: O(N)
        S: O(N)
        :param root:
        :return:
        """

        def gainFromSubTree(node: Optional[TreeNode]) -> int:
            nonlocal maxGain
            if not node:
                return 0

            gainFromLeft = max(gainFromSubTree(node.left), 0)
            gainFromRight = max(gainFromSubTree(node.right), 0)
            maxGain = max(maxGain, gainFromLeft + gainFromRight + node.val)
            return max(gainFromRight + node.val, gainFromLeft + node.val)

        maxGain = -inf
        gainFromSubTree(root)
        return maxGain
