from typing import Optional, List



class TreeNode:


    def __init__(self, val: int = -1, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:


    def generate_trees(self, n: int) -> List[Optional[TreeNode]]:
        """
        Approach: Recursion
        T: O(4^n / sqrt(n))
        S: O(E(n, k - 1) [(n - k + 1) * 4^k / sqrt(k)])
        -----------------------------------------------------------
        Intuition:
        n = 3
        Step1:                 Step 2:         Step 3:
        left SubTree Size  |  root values   | right SubTree Size
        -----------------------------------------------------------
            0              | '1'  2   3     |     2
            1              | 1   '2'  3     |     1
            2              | 1   2   '3'    |     0
        ------------------------------------------------------------
        * left will be from (i - 1)
        * right will be from (n - i)
        ------------------------------------------------------------
        :param n:
        :return:
        """

        memo = [[] for _ in range(n + 1)]
        return self._helper(n, memo)

    def _helper(self, n: int, memo: List[List[int]]) -> List[Optional[TreeNode]]:

        if n == 0:
            return [None]
        if memo[n]:
            return memo[n]
        result = []
        for i in range(1, n + 1):

            left = self._helper(i - 1, memo)
            right = self._helper(n - i, memo)

            right_trees = []

            for right_node in right:
                right_trees.append(self._change_val(right_node, i))

            for left_node in left:
                for right_node in right_trees:

                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    result.append(root)
        memo[n] = result
        return memo[n]

    def _change_val(self, root: Optional[TreeNode], i: int) -> Optional[TreeNode]:

        if not root:
            return root

        new_root = TreeNode(root.val + i)
        new_root.left = self._change_val(root.left, i)
        new_root.right = self._change_val(root.right, i)
        return new_root